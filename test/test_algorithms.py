from flucoma import fluid
from flucoma.utils import get_buffer
from scipy.io import wavfile
from pathlib import Path
import numpy as np
import os

test_file = "test_file.wav"

# slicers
def test_transientslice():
    output = fluid.transientslice(test_file)
    result = get_buffer(output)
    os.remove(output)
    tolerance = 25
    assert len(result) == 1
    assert result[0] - 512 <= tolerance
    assert result[0] != -1.0

def test_noveltyslice():
    output = fluid.noveltyslice(test_file, fftsettings=[128, 64, -1], threshold=0.05)
    result = get_buffer(output)
    os.remove(output)
    tolerance = 128 #one hop
    assert len(result) == 1
    assert result[0] - 512 <= tolerance
    assert result[0] != -1.0


def test_ampslice():
    output = fluid.ampslice(test_file, onthreshold=-24)
    result = get_buffer(output)
    os.remove(output)
    tolerance = 10
    assert len(result) == 1
    assert result[0] - 818 <= tolerance
    assert result[0] != -1.0

def test_ampgate():
    output = fluid.ampgate(test_file)
    result = get_buffer(output)
    os.remove(output)
    assert len(result) == 2
    assert result[0][0] == 511
    assert result[1][0] == 1023
