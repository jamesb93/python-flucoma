from typing import NamedTuple

class NMFReturn(NamedTuple):
    resynth:str = ''
    bases:str = ''
    activations:str = ''

class HPSSReturn(NamedTuple):
    harmonic:str = ''
    percussive:str = ''

class HPSSResidualReturn(NamedTuple):
    harmonic:str = ''
    percussive:str = ''
    residual:str = ''

class SinesReturn(NamedTuple):
    sines:str = ''
    residual:str = ''

class TransientsReturn(NamedTuple):
    transients:str = ''
    residual:str = ''

class STFTReturn(NamedTuple):
    magnitude:str = ''
    phase:str = ''

class InverseSTFTReturn(NamedTuple):
    resynth:str = ''