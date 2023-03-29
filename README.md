# python-flucoma

![run tests automatically each push](https://github.com/jamesb93/python-flucoma/workflows/run%20tests%20automatically%20each%20push/badge.svg?event=push)

Very loose bindings from Python3 to [FluCoMa](https://www.flucoma.org) CLI tools.

> **Warning**
> You need to be using Python 3.10+ as I make use of the new typing features.

You will need to download the command line versions and put them somewhere in your path.

They can be downloaded from [here](https://www.flucoma.org/download/) or compiled from [source](https://github.com/flucoma/flucoma-cli).

With these bindings I tried to replicate the buffer based behaviour that is present across their supported CCE's instead of any magic to produce a 'native' feel to the code.
Instead, functions are bound to `fluid` processes which return where the outputs are. It is then you're job to collect the results.

Examples can be found in this repository under the examples folder.

---

Can be installed by any of the methods:

1. `pip install python-flucoma`
2. `pip install git+https://github.com/jamesb93/python-flucoma`
3. Cloning this repo, `cd` and call `pip install .`
