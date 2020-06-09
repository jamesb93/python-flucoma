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
		"-maxkernelsize", kernelsize,
		"-maxfftsize", str(fftsize),
		"-maxfiltersize", str(filtersize),
		"-source", str(source),
		"-indices", str(indices),
		"-feature", str(feature),
		"-threshold", str(threshold),
		"-fftsettings", str(fftsettings[0]), str(fftsettings[1]), str(fftsize),
		"-minslicelength", str(minslicelength),
		"-filtersize", str(filtersize)
	])

	assert os.path.exists(indices)
	return indices



