from pathlib import Path
from flucoma import fluid
from flucoma.utils import get_buffer


source = Path("Nicol-LoopE-M.wav")

# It might be the case that you want to store the outputs of each process in a specific place
# By specifiying the outputs you don't need to even return anything from a fluid.processor()
resynth = Path("resynth.wav")
activations = Path("activations.wav")
bases = Path("bases.wav")

fluid.nmf(source, 
    resynth=resynth, 
    activations=activations, 
    bases=bases,
    components=2,
    iterations=50,
    fftsettings=[256, 128, 256])
# this would push the outputs to the location on disk
# which can then be referenced elsewhere

stats = get_buffer(bases)
print(stats)

# This could also be useful for caching your processing.
# You might check if something already exists and then skip reprocessing to save time.

