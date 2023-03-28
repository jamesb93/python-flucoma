import shutil
from flucoma.utils import (
    check_compatible_version,
    compute_cli_call,
    exec_cli_call
)
from flucoma.exceptions import BinError
from flucoma.core import (
    FluidSingleOutput,
    HPSSOutput,
    NMFOutput,
    SinesOutput,
    TransientsOutput,
)

if not shutil.which("fluid-noveltyslice"):
    raise BinError("FluCoMa cli tools are not installed!")

check_compatible_version(105)

def noveltyslice(
    source: str | FluidSingleOutput,
    indices: str = "",
    algorithm: int = 0,
    threshold: float = 0.5,
    filtersize: int = 1,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    kernelsize: int = 3,
    minslicelength: int = 2,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('noveltyslice', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def transientslice(
    source: str | FluidSingleOutput,
    indices: str = "",
    blocksize: int = 256,
    clumplength: int = 25,
    minslicelength: int = 100,
    order: int = 20,
    padsize: int = 128,
    skew: float = 0.0,
    threshback: float = 1.1,
    threshfwd: float = 2.0,
    windowsize: int = 14,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('transientslice', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def ampslice(
    source: str | FluidSingleOutput,
    indices: str = "",
    fastrampdown: int = 1,
    fastrampup: int = 1,
    slowrampdown: int = 100,
    slowrampup: int = 100,
    floor: float = -144.0,
    highpassfreq: float = 85.0,
    offthreshold: float = -144.0,
    onthreshold: float = 144.0,
    minslicelength: int = 2,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('ampslice', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def ampgate(
    source: str | FluidSingleOutput,
    indices: str = "",
    rampup: int = 10,
    rampdown: int = 10,
    highpassfreq: float = 85.0,
    lookahead: int = 0,
    lookback: int = 0,
    minlengthabove: int = 1,
    minlengthbelow: int = 1,
    minsilencelength: int = 1,
    minslicelength: int = 1,
    offthreshold: float = -90,
    onthreshold: float = -90,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('ampgate', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def onsetslice(
    source: str | FluidSingleOutput,
    indices: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    filtersize: int = 5,
    framedelta: int = 0,
    metric: int = 0,
    minslicelength: int = 2,
    threshold: float = 0.5,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:

    cli, output = compute_cli_call('onsetslice', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def sines(
    source: str | FluidSingleOutput,
    sines: str = "",
    residual: str = "",
    bandwidth: int = 76,
    birthhighthreshold: float = -60.0,
    birthlowthreshold: float = -24,
    detectionthreshold: float = -96,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    mintracklen: int = 15,
    trackfreqrange: float = 50.0,
    trackmethod: int = 0,
    trackmagrange: float = 15,
    trackprob: float = 0.5,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> SinesOutput:
    cli, output = compute_cli_call('sines', locals())
    exec_cli_call(cli)
    return SinesOutput(output[0], output[1])


def transients(
    source: str | FluidSingleOutput,
    transients: str = "",
    residual: str = "",
    blocksize: int = 256,
    clumplength: int = 25,
    order: int = 20,
    padsize: int = 128,
    skew: float = 0.0,
    threshback: float = 1.1,
    threshfwd: float = 2.0,
    windowsize: int = 14,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> TransientsOutput:
    
    cli, output = compute_cli_call('transients', locals())
    exec_cli_call(cli)
    return TransientsOutput(output[0], output[1])


def hpss(
    source: str | FluidSingleOutput,
    harmonic: str = "",
    percussive: str = "",
    residual: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    harmfiltersize: int = 17,
    percfiltersize: int = 31,
    harmthresh: list[float] = [0.0, 1.0, 1.0, 1.0],
    percthresh: list[float] = [0.0, 1.0, 1.0, 1.0],
    maskingmode: int = 0,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> HPSSOutput:
    cli, output = compute_cli_call('hpss', locals())
    exec_cli_call(cli)
    if maskingmode == 0:
        return HPSSOutput(output[0], output[1])
    else:
        return HPSSOutput(output[0], output[1], output[2])


# Objects
def nmf(
    source: str | FluidSingleOutput,
    resynth: str = "",
    bases: str = "",
    activations: str = "",
    actmode: int = 0,
    basesmode: int = 0,
    components: int = 0,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    iterations: int = 100,
    resynthmode: int = 1,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> NMFOutput:
    cli, output = compute_cli_call('nmf', locals())
    exec_cli_call(cli)
    return NMFOutput(output[0], output[1], output[2])


# Descriptors
def mfcc(
    source: str | FluidSingleOutput,
    features: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    maxfreq: float = 20000.0,
    minfreq: float = 20.0,
    numbands: int = 40,
    numcoeffs: int = 13,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('mfcc', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def loudness(
    source: str | FluidSingleOutput,
    features: str = "",
    hopsize: int = 512,
    windowsize: int = 1024,
    kweighting: int = 1,
    truepeak: int = 1,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('loudness', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def pitch(
    source: str | FluidSingleOutput,
    features: str = "",
    algorithm: int = 2,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    maxfreq: float = 10000.0,
    minfreq: float = 20.0,
    unit: int = 0,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('pitch', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def melbands(
    source: str | FluidSingleOutput,
    features: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    maxfreq: float = 10000.0,
    minfreq: float = 20.0,
    normalize: int = 1,
    numbands: int = 40,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('melbands', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def spectralshape(
    source: str | FluidSingleOutput,
    features: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('spectralshape', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def stats(
    source: str | FluidSingleOutput,
    stats: str = "",
    high: float = 100.0,
    low: float = 0.0,
    middle: float = 50.0,
    numderivs: int = 0,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('stats', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def ampfeature(
    source: str | FluidSingleOutput,
    features: str = "",
    fastrampup: int = 1,
    fastrampdown: int = 1,
    slowrampup: int = 100,
    slowrampdown: int = 100,
    floor: float = -60,
    highpassfreq: float = 85,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('ampfeature', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def noveltyfeature(
    source: str | FluidSingleOutput,
    features: str = "",
    padding: int = 0,
    algorithm: int = 0,
    kernelsize: int = 3,
    filtersize: int = 1,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('noveltyfeature', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def onsetfeature(
    source: str | FluidSingleOutput,
    features: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    filtersize: int = 5,
    framedelta: int = 0,
    metric: int = 0,
    padding: int = 0,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    cli, output = compute_cli_call('onsetfeature', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def audiotransport(
    sourcea: str | FluidSingleOutput,
    sourceb: str | FluidSingleOutput,
    destination: str = "",
    numchansa: int = -1,
    numframesa: int = -1,
    startchana: int = 0,
    startframea: int = 0,
    numchansb: int = -1,
    numframesb: int = -1,
    startchanb: int = 0,
    startframeb: int = 0,
    interpolation: float = 0.5,
    fftsettings: list[int, int, int] = [1024, -1, -1],
) -> FluidSingleOutput:
    cli, output = compute_cli_call('audiotransport', locals())
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])


def nmfcross(
    source: str | FluidSingleOutput,
    target: str | FluidSingleOutput,
    output: str = "",
    timesparsity: int = 7,
    polyphony: int = 11,
    continuity: int = 7,
    iterations: int = 100,
    fftsettings: list[int, int, int] = [1024, -1, -1]
) -> FluidSingleOutput:
    cli, output = compute_cli_call('nmfcross', locals())
    print(cli)
    exec_cli_call(cli)
    return FluidSingleOutput(output[0])