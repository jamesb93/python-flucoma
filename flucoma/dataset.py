from .exceptions import DatasetPointError

def pack(d: dict):
    """
    Reformats a dictionary into a fluid.dataset~
    Two things need to be true for this to work
    - The keys are max compatible symbols for datasets
    - The values in the python dict are flat and can be unpacked with a single iterator
    """
    v = [v for v in d.values()]
    cols = len(v[0])
    
    for x in v:
        if not len(x) == cols:
            raise DatasetPointError("The dimensions for each key need to be uniform.")

    dataset = {
        "cols" : cols,
        "data" : d
    }

    return dataset
