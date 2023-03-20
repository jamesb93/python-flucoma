from pathlib import Path
from flucoma import fluid
from flucoma.utils import cleanup

# You will need to replace the path here with your own sound file
source = Path("stereo_test.wav")

# Take the MFCCs of the source
mfcc = fluid.mfcc(source, numcoeffs=5, numbands=20)

# fluid.processes return a python dataclass that contains two things:
# 1. The file_path which is a string pointing to the file which exists on disk.
# 2. The data stored in that file.
# If you do not pass a specific path for an output it will put the output in a temporary file
# The default location for all output files is temporary location is ~/.python-flucoma

# From the dataclass we can extract

# Wrap a fluid.process() in a get_buffer to get a fairly native output
stats = fluid.stats(mfcc, numderivs=0)

# Let's see the data
for i, band in enumerate(stats):
    printout = f"Stats for MFCC band number {i}: {band} \n"
    print(printout)
print("You should see 10 values for each band's statistics, because we have 5 coefficients and the input is stereo!")


# We didn't set any specific output so we can cleanup the temporary file if we want
cleanup()
