from typing import List
from uuid import uuid4
from .utils import odd_snap, fftformat
from .exceptions import BinError
import tempfile
import os
import subprocess
import shutil

if not shutil.which("fluid-noveltyslice"):
	raise BinError("FluCoMa cli tools are not installed!")

def noveltyslice(
	source:str,
	indices:str = "",
	feature:int = 0,
	threshold:float = 0.5,
	filtersize:int = 1,
	fftsettings:List[int] = [1024, -1, 1024],
	kernelsize:int = 3,
	minslicelength:int = 2) -> str:

	if indices == "":
		tmp = tempfile.mkdtemp()
		uuid = str(uuid4().hex)
		indices = os.path.join(tmp, f"{uuid}.wav")
	
	kernelsize = odd_snap(kernelsize)
	fftsize = fftformat(fftsettings)

	subprocess.call([
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
		"-filtersize", str(filtersize)
		"-numchans", str(numchans),
		"-numframes", str(numframes),
		"-startchan", str(startchan),
		"-startframe", str(startframe)
	])

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



