from flucoma import fluid
from pathlib import Path, PosixPath
from flucoma.core import FluidSingleOutput


test_file = (Path(".") / "test" / "test_file.wav").resolve()

mfcc = fluid.mfcc(test_file)
noveltyslice = fluid.noveltyslice(test_file)
transientslice = fluid.transientslice(test_file)
ampslice = fluid.ampslice(test_file)
ampgate = fluid.ampgate(test_file)
onsetslice = fluid.onsetslice(test_file)
sines = fluid.sines(test_file)
transients = fluid.transients(test_file)
hpss = fluid.hpss(test_file)
nmf = fluid.nmf(test_file)
loudness = fluid.loudness(test_file)
pitch = fluid.pitch(test_file)
melbands = fluid.melbands(test_file)
spectralshape = fluid.spectralshape(test_file)
stats = fluid.stats(test_file)

all_algorithms = [
	mfcc,
	noveltyslice,
	transientslice,
	ampslice,
	ampgate,
	onsetslice,
	sines,
	transients,
	hpss,
	nmf,
	loudness,
	pitch,
	melbands,
	spectralshape,
	stats
]


def test_list():
	'''tests that all outputs can be converted to lists'''
	for algo in all_algorithms:
		if (isinstance(algo, FluidSingleOutput)):
			assert isinstance(list(algo), list)
		else:
			for output in algo:
				assert isinstance(list(output), list)

def test_pathlib():
	for algo in all_algorithms:
		if (isinstance(algo, FluidSingleOutput)):
			p = Path(algo)
			assert isinstance(p, PosixPath)
			assert str(p) != ''
		else:
			for output in algo:
				p = Path(output)
				assert isinstance(p, PosixPath)
				assert str(p) != ''