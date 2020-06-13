import collections

nmf_return = collections.namedtuple('nmf', 'resynth bases activations')
hpss_return = collections.namedtuple('hpss', 'harmonic percussive residual')
sines_return = collections.namedtuple('sines', 'sines residual')
transients_return = collections.namedtuple('transients', 'transients residual')