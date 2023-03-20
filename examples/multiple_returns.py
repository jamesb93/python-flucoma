from pathlib import Path
from flucoma import fluid
from flucoma.fluid import HPSSOutput

source = Path("Nicol-LoopE-M.wav")

# Run HPSS on the source and return a custom DataClass
hpss = fluid.hpss(source)

# Retrieve the outputs by name
harmonic = hpss.harmonic
percussive = hpss.percussive
residual = hpss.residual

# This allows you to work programatically on the outputs

for x in hpss:
    # As it stands these bindings return a path for everything, even if it wasnt made
    # HPSS can return either 2 or 3 things depending on the mode its in
    # So its worth checking that in this case the residual was made
    # If it wasn't it would be a blank string so we just don't process these
    print(x)
    if x != '':
        sines = fluid.sines(x) #The path printed here can be passed to something else for processing
    print(sines.sines)
    print(sines.residual)
