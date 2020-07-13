from .exceptions import DatasetPointError

def pack(d: dict):
    """
    Reformats a dictionary into a fluid.dataset~
    Two things need to be true for this to work
    - The keys are max compatible symbols for datasets
    - The values in the python dict are flat and can be unpacked with a single iterator
    """
    k = [k for k in d.keys()]
    v = [v for v in d.values()]
    cols = len(v[0])
    data = []
    for r in v:
        if not len(r) == cols:
            raise DatasetPointError("Dataset points must be a uniform size")
        for x in r:
            data.append(x)

    dataset = {
        "rows" : len(d),
        "cols" : cols,
        "ids" : k
    }
    dataset["data"] = data
    return dataset
