from typing import List
from uuid import uuid4
from .utils import odd_snap, fftformat, make_temp, handle_ret
from .exceptions import BinError
from .returns import (
	NMFReturn,
	TransientsReturn,
	HPSSReturn,
	SinesReturn
)
import os
import subprocess
import shutil

if not shutil.which("fluid-noveltyslice"):
	raise BinError("FluCoMa cli tools are not installed!")

# Slicing
def noveltyslice(
	source:str,
	indices:str = "",
	feature:int = 0,
	threshold:float = 0.5,
	filtersize:int = 1,
	fftsettings:List[int] = [1024, -1, 1024],
	kernelsize:int = 3,
	minslicelength:int = 2,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)
	if indices == "": indices = make_temp()
	
	kernelsize = odd_snap(kernelsize)
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-noveltyslice",
		"-maxkernelsize", str(kernelsize),
		"-maxfftsize", str(fftsize),
		"-maxfiltersize", str(filtersize),
		"-source", str(source),
		"-indices", str(indices),
		"-feature", str(feature),
		"-threshold", str(threshold),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-minslicelength", str(minslicelength),
		"-filtersize", str(filtersize),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)

	assert os.path.exists(indices)
	return indices

def transientslice(
	source:str,
	indices:str = "",
	blocksize:int = 256,
	clumplength:int = 25,
	minslicelength:int = 100,
	order:int = 20,
	padsize:int = 128,
	skew:float = 0.0,
	threshback:float = 1.1,
	threshfwd:float = 2.0,
	windowsize:int = 14,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if indices == "": indices = make_temp()

	ret = subprocess.call([
		"fluid-transientslice",
		"-source", str(source),
		"-indices", str(indices),
		"-blocksize", str(blocksize),
		"-clumplength", str(clumplength),
		"-minslicelength", str(minslicelength),
		"-order", str(order),
		"-padsize", str(padsize),
		"-skew", str(skew),
		"-threshback", str(threshback),
		"-threshfwd", str(threshfwd),
		"-windowsize", str(windowsize),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(indices)
	return indices

def ampslice(
	source:str,
	indices:str = "",
	fastrampdown:int = 1,
	fastrampup:int = 1,
	slowrampdown:int = 100,
	slowrampup:int = 100,
	floor:float = -144.0,
	highpassfreq:float = 85.0,
	offthreshold:float = -144.0,
	onthreshold:float = 144.0,
	minslicelength:int = 2,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if indices == "": indices = make_temp()

	ret = subprocess.call([
		"fluid-ampslice",
		"-source", str(source),
		"-indices", str(indices),
		"-fastrampdown", str(fastrampdown),
		"-fastrampup", str(fastrampup),
		"-slowrampdown", str(slowrampdown),
		"-slowrampup", str(slowrampup),
		"-floor", str(floor),
		"-highpassfreq", str(highpassfreq),
		"-offthreshold", str(offthreshold),
		"-onthreshold", str(onthreshold),
		"-minslicelength", str(minslicelength),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(indices)
	return indices

def ampgate(
	source:str,
	indices:str = "",
	rampup:int = 10,
	rampdown:int = 10,
	highpassfreq:float = 85.0,
	lookahead:int = 0,
	lookback:int = 0,
	minlengthabove:int = 1,
	minlengthbelow:int = 1,
	minsilencelength:int = 1,
	minslicelength:int = 1,
	offthreshold:float = -144.0,
	onthreshold:float = 144.0,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if indices == "": indices = make_temp()

	ret = subprocess.call([
		"fluid-ampgate",
		"-source", str(source),
		"-indices", str(indices),
		"-rampup", str(rampup),
		"-rampdown", str(rampdown),
		"-highpassfreq", str(highpassfreq),
		"-lookahead", str(lookahead),
		"-lookback", str(lookback),
		"-minlengthabove", str(minlengthabove),
		"-minlengthbelow", str(minlengthbelow),
		"-minsilencelength", str(minsilencelength),
		"-minslicelength", str(minslicelength),
		"-offthreshold", str(offthreshold),
		"-onthreshold", str(onthreshold),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(indices)
	return indices

def onsetslice(
	source:str,
	indices:str = "",
	fftsettings:List[int] = [1024, -1, -1],
	filtersize:int = 5,
	framedelta:int = 0,
	metric:int = 0,
	minslicelength:int = 2,
	threshold:float = 0.5,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if stats == "": stats = make_temp()

	fftsize = fftformat(fftsettings)
	filtersize = odd_snap(filtersize)

	ret = subprocess.call([
		"fluid-onsetslice",
		"-maxfftsize", fftsize,
		"-source", str(source),
		"-indices", str(indices),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-filtersize", str(filtersize),
		"-framedelta", str(framedelta),
		"-metric", str(metric),
		"-minslicelength", str(minslicelength),
		"-threshold", str(threshold),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(indices)
	return stats

# Layers
def sines(
	source:str,
	sines:str = "",
	residual:str = "",
	bandwidth:int = 76,
	birthhighthreshold:float = -60.0,
	birthlowthreshold:float = -24,
	detectionthreshold:float = -96,
	fftsettings:List[int] = [1024, -1, -1],
	mintracklen:int = 15,
	trackfreqrange:float = 50.0,
	trackingmethod:int = 0,
	trackmagrange:float = 15,
	trackprob:float = 0.5,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if sines == "": sines = make_temp()
	if residual == "": residual = make_temp()
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-sines",
		"-maxfftsize", fftsize,
		"-source", str(source),
		"-sines", str(sines),
		"-residual", str(residual),
		"-bandiwdth", str(bandwidth),
		"-birthhighthreshold", str(birthhighthreshold),
		"-birthlowthreshold", str(birthlowthreshold),
		"-detectionthreshold", str(detectionthreshold),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-mintracklen", str(mintracklen),
		"-trackfreqrange", str(trackfreqrange),
		"-trackingmethod", str(trackingmethod),
		"-trackmagrange", str(trackmagrange),
		"-trackprob", str(trackprob),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(sines)
	assert os.path.exists(residual)
	return SinesReturn(sines, residual)

def transients(
	source:str,
	transients:str = "",
	residual:str = "",
	blocksize:int = 256,
	clumplength:int = 25,
	order:int = 20,
	padsize:int = 128,
	skew:float = 0.0,
	threshback:float = 1.1,
	threshfwd:float = 2.0,
	windowsize:int = 14,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> TransientsReturn:

	assert os.path.exists(source)

	if transients == "": transients = make_temp()
	if residual == "": residual = make_temp()

	ret = subprocess.call([
		"fluid-transients",
		"-source", str(source),
		"-transients", str(transients),
		"-residual", str(residual),
		"-blocksize", str(blocksize),
		"-clumplength", str(clumplength),
		"-order", str(order),
		"-padsize", str(padsize),
		"-skew", str(skew),
		"-threshback", str(threshback),
		"-threshfwd", str(threshfwd),
		"-windowsize", str(windowsize),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(transients)
	assert os.path.exists(residual)
	return TransientsReturn(transients, residual)

def hpss(
	source:str,
	harmonic:str = "",
	percussive:str = "",
	residual:str = "",
	fftsettings:List[int] = [1024, -1, -1],
	harmfiltersize:int = 17,
	percfiltersize:int = 31,
	harmthresh:List[float] = [0.0, 1.0, 1.0, 1.0],
	percthresh:List[float] = [0.0, 1.0, 1.0, 1.0],
	maskingmode:int = 0,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> HPSSReturn:

	assert os.path.exists(source)

	if harmonic == "": harmonic = make_temp()
	if percussive == "": percussive = make_temp()
	if residual == "": residual = make_temp()

	fftsize = fftformat(fftsettings)

	harmfiltersize = odd_snap(harmfiltersize)
	percfiltersize = odd_snap(percfiltersize)

	ret = subprocess.call([
		"fluid-hpss",
		"-source", str(source),
		"-harmonic", str(harmonic),
		"-percussive", str(percussive),
		"-residual", str(residual),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-harmfiltersize", str(harmfiltersize),
		"-percfiltersize", str(percfiltersize),
		"-harmthresh", str(harmthresh[0]), str(harmthresh[1]), str(harmthresh[2]), str(harmthresh[3]),
		"-percthresh", str(percthresh[0]), str(percthresh[1]), str(percthresh[2]), str(percthresh[3]),
		"-maskingmode", str(maskingmode),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(harmonic)
	assert os.path.exists(percussive)
	if maskingmode != 0: 
		assert os.path.exists(residual)
	if maskingmode == 0: 
		return HPSSReturn(harmonic, percussive)
	else: 
		return HPSSReturn(harmonic, percussive, residual)

# Objects
def nmf(
	source:str,
	activations:str = "",
	bases:str = "",
	resynth:str = "",
	actmode:int = 0,
	basesmode:int = 0,
	components:int = 0,
	fftsettings:List[int] = [1024, -1, -1],
	iterations:int = 100,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> NMFReturn:

	assert os.path.exists(source)

	if activations == "": activations = make_temp()
	if bases == "": bases  = make_temp()
	if resynth == "": resynth  = make_temp()

	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-nmf",
		"-source", str(source),
		"-activations", str(activations),
		"-bases", str(bases),
		"-resynth", str(resynth),
		"-actmode", str(actmode),
		"-basesmode", str(basesmode),
		"-components", str(components),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-iterations", str(iterations),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(resynth)
	assert os.path.exists(activations)
	assert os.path.exists(bases)
	return NMFReturn(resynth, bases, activations)

# Descriptors
def mfcc(
	source:str,
	features:str = "",
	fftsettings:List[int] = [1024, -1, -1],
	maxfreq:float = 20000.0,
	minfreq:float = 20.0,
	numbands:int = 40,
	numcoeffs:int = 13,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if features == "": features = make_temp()
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-mfcc",
		"-maxnumcoeffs", str(numcoeffs),
		"-maxfftsize", str(fftsize),
		"-source", str(source),
		"-features", str(features),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-maxfreq", str(maxfreq),
		"-minfreq", str(minfreq),
		"-numbands", str(numbands),
		"-numcoeffs", str(numcoeffs),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(features)
	return features

def loudness(
	source:str,
	features:str = "",
	hopsize:int = 512,
	windowsize:int = 1024,
	kweighting:int = 1,
	truepeak:int = 1,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if features == "": features = make_temp()

	ret = subprocess.call([
		"fluid-loudness",
		"-source", str(source),
		"-features", str(features),
		"-hopsize", str(hopsize),
		"-windowsize", str(windowsize),
		"-kweighting", str(kweighting),
		"-truepeak", str(truepeak),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(features)
	return features

def pitch(
	source:str,
	features:str = "",
	algorithm:int = 2,
	fftsettings:List[int] = [1024, -1, -1],
	maxfreq:float = 10000.0,
	minfreq:float = 20.0,
	unit:int = 0,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if features == "": features = make_temp()
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-pitch",
		"-maxfftsize", str(fftsize),
		"-source", str(source),
		"-features", str(features),
		"-algorithm", str(algorithm),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-maxfreq", str(maxfreq),
		"-minfreq", str(minfreq),
		"-unit", str(unit),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(features)
	return features

def melbands(
	source:str,
	features:str = "",
	fftsettings:List[int] = [1024, -1, -1],
	maxfreq:float = 10000.0,
	minfreq:float = 20.0,
	normalize:int = 1,
	numbands:int = 40,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if features == "": features = make_temp()
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-melbands",
		"-maxnumbands", str(numbands),
		'-maxfftsize', str(fftsize),	
		"-source", str(source),
		"-features", str(features),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-maxfreq", str(maxfreq),
		"-minfreq", str(minfreq),
		"-normalize", str(normalize),
		"-numbands", str(numbands),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(features)
	return features

def spectralshape(
	source:str,
	features:str = "",
	fftsettings:List[int] = [1024, -1, -1],
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if features == "": features = make_temp()
	fftsize = fftformat(fftsettings)

	ret = subprocess.call([
		"fluid-spectralshape",
		'-maxfftsize', str(fftsize),	
		"-source", str(source),
		"-features", str(features),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(features)
	return features


def stats( 
	source:str,
	stats:str = "",
	high:float = 100.0,
	low:float = 0.0,
	middle:float = 50.0,
	numderivs:int = 0,
	numchans:int = -1,
	numframes:int = -1,
	startchan:int = 0,
	startframe:int = 0) -> str:

	assert os.path.exists(source)

	if stats == "": stats = make_temp()

	ret = subprocess.call([
		"fluid-stats",
		"-source", str(source),
		"-stats", str(stats),
		"-high", str(high),
		"-low", str(low),
		"-middle", str(middle),
		"-numderivs", str(numderivs),
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

	handle_ret(ret)
	assert os.path.exists(stats)
	return stats