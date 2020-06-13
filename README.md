# python-flucoma

Very loose functional programming bindings from Python3 to [FluCoMa](https://www.flucoma.org) CLI tools.

You will need to download the command line versions and put them somewhere in your path.

With these bindings I tried to replicate the buffer based behaviour that is present across their supported CCE's instead of any magic to produce a 'native' feel to the code.
Instead, functions are bound to `fluid` processes which return where the outputs are. It is then you're job to collect the results.

A basic novelty slice call is something like:

```python
from flucoma import fluid
from flucoma.utils import get_slices
from pathlib import Path

source = Path("~/Desktop/ec1.wav").expanduser().resolve()

ns = fluid.noveltyslice(source, threshold=0.1)
idx = get_buffer(ns)

print(idx)
```

or for a more complex example chaining together the output of one process as the input of the next.

```python
from flucoma import fluid
from flucoma.utils import get_slices


mfcc = fluid.mfcc(source, 
    fftsettings = [2048, -1, -1],
    startframe = start,
    numframes = length
)

stats = get_buffer(
    fluid.stats(mfcc,
        numderivs = 1
    ), "numpy" # get_buffer() can return numpy arrays too
)

print(stats)
```

Can be installed by any of the methods:

1. Cloning this repo, `cd` and call `pip install .`
2. `pip install git+https://github.com/jamesb93/python-flucoma`
3. Soon PyPi


