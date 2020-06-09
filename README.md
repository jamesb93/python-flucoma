# python-flucoma

Very loose functional programming bindings from Python3 to [FluCoMa](https://www.flucoma.org) CLI tools.

With these bindings I tried to replicate the buffer based behaviour that is present across their supported CCE's instead of any magic to produce a 'native' feel to the code.
Instead, functions are bound to `fluid` processes which return where the outputs are. It is then you're job to collect the results.

A basic novelty slice call is something like:

```python
from flucoma import fluid
from flucoma.utils import get_slices, odd_snap
from pathlib import Path

source = Path("~/Desktop/ec1.wav").expanduser().resolve()

ns = fluid.noveltyslice(source, threshold=0.1)
idx = get_slices(ns, "numpy")

print(idx)
```

Can be installed by any of the methods:

1. Cloning this repo, `cd` and call `pip install .`
2. `pip install git+https://github.com/jamesb93/python-flucoma`
3. Soon PyPi


