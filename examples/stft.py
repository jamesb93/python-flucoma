from pathlib import Path
from flucoma import fluid
from flucoma.utils import cleanup


# Perform a STFT analysis on a sound file
source = Path("Nicol-LoopE-M.wav")
stft = fluid.stft(source)

# Reconstruct the soundfile by passing a magnitude and phase and setting inverse=True
inverse = fluid.stft(source, 
    inverse=True, 
    magnitude=stft.magnitude, 
    phase=stft.phase
)

cleanup() 

