import soundfile as sf
import math
from uuid import uuid4
from typing import List
from .exceptions import ShellError
from pathlib import Path

def fftsanitise(fftsettings) -> List[int]:
    return [
        int(fftsettings[0]),
        int(fftsettings[1]), 
        int(fftsettings[2])
    ]

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

def fftformat(fftsettings: List[int]) -> int:
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
    