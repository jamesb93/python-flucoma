import numpy as np
import os
from random import random
from scipy.io import wavfile
from pathlib import Path
from flucoma import fluid
from flucoma.utils import (
    get_buffer,
    odd_snap,
    fft_format,
    make_temp,
    fft_sanitise,
    cleanup,
    parse_version,
)


def test_parse_version():
    ex1 = "The Fluid Corpus Manipulation Toolkit has version 1.0.5+sha.fab75e7.core.sha.001df55a\n"
    ex2 = "The Fluid Corpus Manipulation Toolkit has version 1.1.0+sha.fab75e7.core.sha.001df55a\n"
    ex3 = "The Fluid Corpus Manipulation Toolkit has version 3.0.0+sha.fab75e7.core.sha.001df55a\n"
    ex4 = "The FluCoMa Toolkit has version 1.0.5+sha.fab75e7.core.sha.001df55a\n"

    v1 = parse_version(ex1)
    v2 = parse_version(ex2)
    v3 = parse_version(ex3)
    v4 = parse_version(ex4)

    assert v1 == 105
    assert v2 == 110
    assert v3 == 300
    assert v4 == 105
    assert v2 > v1


def test_fft_sanitise():
    bad_fft = [512.0, 128.0, 512.0]
    good_fft = fft_sanitise(bad_fft)
    for x in good_fft:
        assert isinstance(x, int)


def test_get_buffer():
    # make a test wave file with some values
    rands = []
    test_file = "random_buffer.wav"
    for _ in range(100):
        rands.append(random())
    wavfile.write(test_file, 44100, np.array(rands))
    assert os.path.exists("random_buffer.wav")
    buflist = get_buffer(test_file)
    bufnp = get_buffer(test_file, "numpy")
    os.remove(test_file)
    assert isinstance(buflist, list)
    assert isinstance(bufnp, np.ndarray)
    assert buflist == rands


def test_odd_snap():
    assert odd_snap(0) == 1
    assert odd_snap(-24) == -23
    assert odd_snap(-23) == -23
    assert odd_snap(2) == 3
    assert odd_snap(512) == 513
    assert odd_snap(1025) == 1025


def test_fft_format():
    caseone = [1024, 512, -1]
    casetwo = [100, 512, -1]
    casethree = [100, 512, -1]
    casefour = [100, 512, 100]
    casefive = [500, -1, -1]
    assert fft_format(caseone) == 1024
    assert fft_format(casetwo) == 128
    assert fft_format(casethree) == 128
    assert fft_format(casefour) == 128
    assert fft_format(casefive) == 512


def test_make_temp():
    temp_file = make_temp()
    another_file = make_temp()
    assert isinstance(temp_file, str)
    assert isinstance(another_file, str)
    assert another_file != temp_file


def test_cleanup():
    tempfiles = Path.home() / ".python-flucoma"
    test_file = Path("test") / "test_file.wav"
    fluid.hpss(test_file)
    cleanup()
    leftovers = [x for x in tempfiles.iterdir() if x != ".DS_Store"]
    assert len(leftovers) == 0
