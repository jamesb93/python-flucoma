import pytest
import numpy as np
import os
from random import random
from scipy.io import wavfile


from flucoma.utils import (
    get_buffer,
    odd_snap,
    fftformat,
    make_temp,
    fftsanitise
)

def test_fftsanitise():
    bad_fft = [512.0, 128.0, 512.0]
    good_fft = fftsanitise(bad_fft)
    for x in good_fft:
        assert type(x) == type(int())

def test_get_buffer():
    # make a test wave file with some values
    rands = []
    test_file = "random_buffer.wav"
    for i in range(100):
        rands.append(random())
    rands_np = np.array(rands)
    wavfile.write(test_file, 44100, np.array(rands))
    assert os.path.exists("random_buffer.wav")
    buflist = get_buffer(test_file)
    bufnp = get_buffer(test_file, "numpy")

    assert type(buflist) == type(list())
    assert type(bufnp) == type(np.zeros((1, 1)))
    assert buflist == rands


def test_odd_snap():
    assert odd_snap(0) == 1
    assert odd_snap(-24) == -23
    assert odd_snap(-23) == -23
    assert odd_snap(2) == 3
    assert odd_snap(512) == 513
    assert odd_snap(1025) == 1025


def test_fftformat():
    caseone = [1024, 512, -1]
    casetwo = [100, 512, -1]
    casethree = [100, 512, -1]
    casefour = [100, 512, 100]
    casefive = [500, -1, -1]
    assert fftformat(caseone) == 1024
    assert fftformat(casetwo) == 128
    assert fftformat(casethree) == 128
    assert fftformat(casefour) == 128
    assert fftformat(casefive) == 512

def test_make_temp():
    temp_file = make_temp()
    another_file = make_temp()
    assert type(temp_file) == type(str())
    assert type(another_file) == type(str())
    assert another_file != temp_file





