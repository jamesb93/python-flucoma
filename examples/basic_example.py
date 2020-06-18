from pathlib import Path
from flucoma import fluid
from flucoma.utils import get_buffer


source = Path("Nicol-LoopE-M.wav")

# Take the MFCCs of the source
mfcc = fluid.mfcc(source, numcoeffs=19, numbands=80, fftsettings=[4096, 512, 4096])

# fluid.processes() return the path to the output file because the CLI binary data
# We then use get_buffer() to convert this file from disk to a python type (list or numpy array)
# No need to store the output of fluid.stats if it is a 'one shot' process. We can pass directly to get_buffer()

# Wrap a fluid.process() in a get_buffer to get a fairly native output
# You can choose between a native python list or numpy array
stats = get_buffer(
    fluid.stats(mfcc, numderivs=1)
)

# Let's see the data
for i, band in enumerate(stats):
    printout = f"Stats for {i+1} MFCC band: {band} \n"
    print(printout)

