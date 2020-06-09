import soundfile as sf
import math
from typing import List

def get_slices(audio_file_path: str, output: str = "list"):
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
    if  fftsize == -1:
        fftsize = fftsettings[0]
    return math.floor(2 ** math.ceil(math.log(fftsize)/math.log(2)))
def make_temp() -> str:
    """Convenience for creating unique temporary files"""
    tmp = tempfile.mkdtemp()
    uuid = str(uuid4().hex)
    return os.path.join(tmp, f"{uuid}.wav")
def handle_ret(retval: int):
    """Handle return value and raise exceptions if necessary"""
    if retval != 0:
        raise ShellError(retval)
