from flucoma import fluid
from flucoma.utils import get_buffer
from scipy.io import wavfile
from pathlib import Path
import numpy as np
import os

test_file = Path(".") / "test" / "test_file.wav"
test_file = test_file.resolve()
test_buf = get_buffer(test_file)

# slicers
def test_transientslice():
    output = fluid.transientslice(test_file)
    result = get_buffer(output)
    os.remove(output)
    tolerance = 14
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

# layers

def test_sines():
    output = fluid.sines(test_file)
    assert Path(output.sines).exists()
    assert Path(output.residual).exists()

    for x in output:
        buf = get_buffer(x)
        assert len(buf) == len(test_buf)

def test_transients():
    output = fluid.transients(test_file)
    assert Path(output.transients).exists()
    assert Path(output.residual).exists()

    for x in output:
        buf = get_buffer(x)
        assert len(buf) == len(test_buf)

def test_hpss_maskingmode2():
    output = fluid.hpss(test_file, maskingmode=2)
    assert Path(output.harmonic).exists()
    assert Path(output.percussive).exists()
    assert Path(output.residual).exists()

    for x in output:
        buf = get_buffer(x)
        assert len(buf) == len(test_buf)

def test_hpss():
    output = fluid.hpss(test_file)
    assert Path(output.harmonic).exists()
    assert Path(output.percussive).exists()

    buf = get_buffer(output.harmonic)
    assert len(buf) == len(test_buf)

    buf = get_buffer(output.percussive)
    assert len(buf) == len(test_buf)

def test_nmf():
    fftsize = 256
    hopsize = fftsize / 2
    output = fluid.nmf(test_file, iterations=1, components=3, fftsettings=[fftsize, hopsize, fftsize])
    resynth     = get_buffer(output.resynth)
    activations = get_buffer(output.activations)
    bases       = get_buffer(output.bases)
    assert len(resynth) == 3
    assert len(activations) == 3
    assert len(bases) == 3

    for x in resynth:
        assert len(x) == len(test_buf)

    for x in bases:
        assert len(x) == fftsize / 2 + 1

    for x in activations:
        assert len(x) == len(test_buf) / hopsize + 1

# descriptors
def test_mfcc():
    fftsize = 256
    hopsize = fftsize / 2
    numcoeffs = 6
    output = fluid.mfcc(
        test_file, 
        numcoeffs=numcoeffs, 
        fftsettings=[fftsize, hopsize, fftsize])
    mfcc = get_buffer(output)
    assert len(mfcc) == numcoeffs
    for x in mfcc:
        assert len(x) == len(test_buf) / hopsize + 1

def test_melbands():
    fftsize = 256
    hopsize = fftsize / 2
    numbands = 6
    output = fluid.melbands(
        test_file, 
        numbands=numbands, 
        fftsettings=[fftsize, hopsize, fftsize])
    melbands = get_buffer(output)
    assert len(melbands) == numbands
    for x in melbands:
        assert len(x) == len(test_buf) / hopsize + 1

def test_spectralshape():
    fftsize = 256
    hopsize = fftsize / 2
    output = fluid.spectralshape(
        test_file,
        fftsettings=[fftsize, hopsize, fftsize])
    shape = get_buffer(output)
    assert len(shape) == 7 # each shape descriptor
    for x in shape:
        assert len(x) == len(test_buf) / hopsize + 1

def test_pitch():
    fftsize = 256
    hopsize = fftsize / 2
    output = fluid.pitch(
        test_file,
        fftsettings=[fftsize, hopsize, fftsize])
    pitch = get_buffer(output)
    assert len(pitch) == 2 # each shape descriptor
    for x in pitch:
        assert len(x) == len(test_buf) / hopsize + 1

def test_stats():
    for i in range(2):
        output = fluid.stats(test_file, numderivs=i)
        stats = get_buffer(output)
        assert len(stats) == (i+1) * 7

def test_loudness():
    output = fluid.loudness(
        source=test_file,
        windowsize=256,
        hopsize=128
    )
    loudness = get_buffer(output)
    assert len(loudness) == 2 # loudness and true peak
    for x in loudness:
        assert len(x) == len(test_buf) / 128 + 1