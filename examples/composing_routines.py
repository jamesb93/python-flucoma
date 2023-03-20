from pathlib import Path
from flucoma import fluid
from flucoma.utils import get_buffer

source = Path("Nicol-LoopE-M.wav")

# Because the returns of fluid.processes() are generic we can compose them into custom classes

class SpectralStats:
    def __init__(self):
        self.mfcc: str = ""
        self.data: list = []

    def process(self, source):
        self.mfcc = fluid.spectralshape(source)
        self.data = get_buffer(fluid.stats(self.mfcc))


# Create an instance of our class
specstats = SpectralStats()

# Run the process method
specstats.process(source)

# Let's see the output
print(specstats.data)
