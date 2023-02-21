import soundfile as sf
import re
import math
import subprocess
from uuid import uuid4
from .exceptions import ShellError, BinVersionIncompatible
from pathlib import Path

def check_compatible_version(minimum_version):
    # Check version of CLI tools is compatible
    flucoma_cli_version = subprocess.run(
        ['fluid-noveltyslice', '--version'], 
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')

    parsed_version = parse_version(flucoma_cli_version)

    if  parsed_version < minimum_version:
        raise BinVersionIncompatible(f'FluCoMa CLI tools need to be greater than or equal to 1.0.5. They are currently {parsed_version}')


def parse_version(version_string: str):
    # regular expression to extract the version number, ignoring any text before it and after it
    pattern = r".*version (\d+\.\d+\.\d+)[^,]*"

    # search for the pattern in the string
    match = re.search(pattern, version_string)

    # extract the version number from the matched object
    version = int(match.group(1).replace('.', ''))
    return version


def fft_sanitise(fftsettings: list[int, int, int]) -> list[int, int, int]:
    return [int(x) for x in fftsettings]

def get_buffer(audio_file_path: str, output: str = "list"):
    """Returns an audio files fp32 values as a numpy array"""
    data, _ = sf.read(audio_file_path)
    data = data.transpose()
    if output == "list":
        return data.tolist()
    if output == "numpy":
        return data

def odd_snap(number: int) -> int:
    """snaps a number to the next odd number"""
    if (number % 2) == 0:
        return number + 1
    else:
        return number

def fft_format(fftsettings: list[int, int, int]) -> int:
    """Handles the FFT size so you can pass maxfftsize"""
    fftsize = fftsettings[2]
    if fftsize == -1:
        fftsize = fftsettings[0]
    return math.floor(2 ** math.ceil(math.log(fftsize)/math.log(2)))

def handle_ret(retval: int):
    """Handle return value and raise exceptions if necessary"""
    if retval != 0:
        raise ShellError(retval)

def make_temp() -> str:
    """Create temporary files in local hidden directory"""
    tempfiles = Path.home() / ".python-flucoma"
    if not tempfiles.exists():
        tempfiles.mkdir()
    
    uuid = str(uuid4().hex)
    full_path = tempfiles / f"{uuid}.wav" 
    return str(full_path)

def cleanup():
    tempfiles = Path.home() / ".python-flucoma"
    if tempfiles.exists():
        for x in tempfiles.iterdir():
            x.unlink()
    