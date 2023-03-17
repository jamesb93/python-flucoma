import subprocess
import shutil
from flucoma.utils import (
    fft_format,
    make_temp,
    handle_ret,
    fft_sanitise,
    check_compatible_version,
    check_source_exists,
    compute_cli_call
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
    check_source_exists(source)
    indices = indices or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)
    ret = subprocess.call(
        [
            "fluid-noveltyslice",
            "-source",
            str(source),
            "-indices",
            str(indices),
            "-algorithm",
            str(algorithm),
            "-threshold",
            str(threshold),
            "-kernelsize",
            str(kernelsize),
            str(kernelsize),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-filtersize",
            str(filtersize),
            str(filtersize),
            "-minslicelength",
            str(minslicelength),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(indices)


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
    check_source_exists(source)

    indices = indices or make_temp()

    ret = subprocess.call(
        [
            "fluid-transientslice",
            "-source",
            str(source),
            "-indices",
            str(indices),
            "-blocksize",
            str(blocksize),
            "-clumplength",
            str(clumplength),
            "-minslicelength",
            str(minslicelength),
            "-order",
            str(order),
            "-padsize",
            str(padsize),
            "-skew",
            str(skew),
            "-threshback",
            str(threshback),
            "-threshfwd",
            str(threshfwd),
            "-windowsize",
            str(windowsize),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(indices)


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
    check_source_exists(source)

    indices = indices or make_temp()

    ret = subprocess.call(
        [
            "fluid-ampslice",
            "-source",
            str(source),
            "-indices",
            str(indices),
            "-fastrampdown",
            str(fastrampdown),
            "-fastrampup",
            str(fastrampup),
            "-slowrampdown",
            str(slowrampdown),
            "-slowrampup",
            str(slowrampup),
            "-floor",
            str(floor),
            "-highpassfreq",
            str(highpassfreq),
            "-offthreshold",
            str(offthreshold),
            "-onthreshold",
            str(onthreshold),
            "-minslicelength",
            str(minslicelength),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(indices)


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
    check_source_exists(source)

    indices = indices or make_temp()

    ret = subprocess.call(
        [
            "fluid-ampgate",
            "-source",
            str(source),
            "-indices",
            str(indices),
            "-rampup",
            str(rampup),
            "-rampdown",
            str(rampdown),
            "-highpassfreq",
            str(highpassfreq),
            "-lookahead",
            str(lookahead),
            "-lookback",
            str(lookback),
            "-minlengthabove",
            str(minlengthabove),
            "-minlengthbelow",
            str(minlengthbelow),
            "-minsilencelength",
            str(minsilencelength),
            "-minslicelength",
            str(minslicelength),
            "-offthreshold",
            str(offthreshold),
            "-onthreshold",
            str(onthreshold),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(indices)


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
    ret = subprocess.call(cli)
    handle_ret(ret)
    return FluidSingleOutput(output)


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
    trackingmethod: int = 0,
    trackmagrange: float = 15,
    trackprob: float = 0.5,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> SinesOutput:
    check_source_exists(source)

    sines = sines or make_temp()
    residual = residual or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-sines",
            "-source",
            str(source),
            "-sines",
            str(sines),
            "-residual",
            str(residual),
            "-bandwidth",
            str(bandwidth),
            "-birthhighthreshold",
            str(birthhighthreshold),
            "-birthlowthreshold",
            str(birthlowthreshold),
            "-detectionthreshold",
            str(detectionthreshold),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-mintracklen",
            str(mintracklen),
            "-trackfreqrange",
            str(trackfreqrange),
            "-trackmethod",
            str(trackingmethod),
            "-trackmagrange",
            str(trackmagrange),
            "-trackprob",
            str(trackprob),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return SinesOutput(sines, residual)


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
    check_source_exists(source)

    transients = transients or make_temp()
    residual = residual or make_temp()

    ret = subprocess.call(
        [
            "fluid-transients",
            "-source",
            str(source),
            "-transients",
            str(transients),
            "-residual",
            str(residual),
            "-blocksize",
            str(blocksize),
            "-clumplength",
            str(clumplength),
            "-order",
            str(order),
            "-padsize",
            str(padsize),
            "-skew",
            str(skew),
            "-threshback",
            str(threshback),
            "-threshfwd",
            str(threshfwd),
            "-windowsize",
            str(windowsize),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return TransientsOutput(transients, residual)


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
    check_source_exists(source)

    harmonic = harmonic or make_temp()
    percussive = percussive or make_temp()
    residual = residual or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-hpss",
            "-source",
            str(source),
            "-harmonic",
            str(harmonic),
            "-percussive",
            str(percussive),
            "-residual",
            str(residual),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-harmfiltersize",
            str(harmfiltersize),
            str(harmfiltersize),
            "-percfiltersize",
            str(percfiltersize),
            str(percfiltersize),
            "-harmthresh",
            str(harmthresh[0]),
            str(harmthresh[1]),
            str(harmthresh[2]),
            str(harmthresh[3]),
            "-percthresh",
            str(percthresh[0]),
            str(percthresh[1]),
            str(percthresh[2]),
            str(percthresh[3]),
            "-maskingmode",
            str(maskingmode),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    if maskingmode == 0:
        return HPSSOutput(harmonic, percussive)
    else:
        return HPSSOutput(harmonic, percussive, residual)


# Objects
def nmf(
    source: str | FluidSingleOutput,
    activations: str = "",
    bases: str = "",
    resynth: str = "",
    actmode: int = 0,
    basesmode: int = 0,
    components: int = 0,
    fftsettings: list[int, int, int] = [1024, -1, -1],
    iterations: int = 100,
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> NMFOutput:
    check_source_exists(source)

    resynth = resynth or make_temp()
    activations = activations or make_temp()
    bases = bases or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)
    ret = subprocess.call(
        [
            "fluid-nmf",
            "-source",
            str(source),
            "-activations",
            str(activations),
            "-bases",
            str(bases),
            "-resynth",
            str(resynth),
            "-resynthmode",
            str(1),
            "-actmode",
            str(actmode),
            "-basesmode",
            str(basesmode),
            "-components",
            str(components),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-iterations",
            str(iterations),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return NMFOutput(resynth, bases, activations)


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
    check_source_exists(source)

    features = features or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-mfcc",
            "-source",
            str(source),
            "-features",
            str(features),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-maxfreq",
            str(maxfreq),
            "-minfreq",
            str(minfreq),
            "-numbands",
            str(numbands),
            str(numbands),
            "-numcoeffs",
            str(numcoeffs),
            str(numcoeffs),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    features = features or make_temp()

    ret = subprocess.call(
        [
            "fluid-loudness",
            "-source",
            str(source),
            "-features",
            str(features),
            "-hopsize",
            str(hopsize),
            "-windowsize",
            str(windowsize),
            "-kweighting",
            str(kweighting),
            "-truepeak",
            str(truepeak),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    features = features or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-pitch",
            "-source",
            str(source),
            "-features",
            str(features),
            "-algorithm",
            str(algorithm),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-maxfreq",
            str(maxfreq),
            "-minfreq",
            str(minfreq),
            "-unit",
            str(unit),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    features = features or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-melbands",
            "-source",
            str(source),
            "-features",
            str(features),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-maxfreq",
            str(maxfreq),
            "-minfreq",
            str(minfreq),
            "-normalize",
            str(normalize),
            "-numbands",
            str(numbands),
            str(numbands),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


def spectralshape(
    source: str | FluidSingleOutput,
    features: str = "",
    fftsettings: list[int, int, int] = [1024, -1, -1],
    numchans: int = -1,
    numframes: int = -1,
    startchan: int = 0,
    startframe: int = 0,
) -> FluidSingleOutput:
    check_source_exists(source)

    features = features or make_temp()
    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-spectralshape",
            "-source",
            str(source),
            "-features",
            str(features),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    stats = stats or make_temp()

    ret = subprocess.call(
        [
            "fluid-stats",
            "-source",
            str(source),
            "-stats",
            str(stats),
            "-high",
            str(high),
            "-low",
            str(low),
            "-middle",
            str(middle),
            "-numderivs",
            str(numderivs),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(stats)


def function_to_cli_string(args):
    for key, value in args.items():
        print(key, value)
    return


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
    check_source_exists(source)

    features = features or make_temp()

    ret = subprocess.call(
        [
            "fluid-ampfeature",
            "-source",
            str(source),
            "-features",
            str(features),
            "-fastrampup",
            str(fastrampup),
            "-fastrampdown",
            str(fastrampdown),
            "-slowrampup",
            str(slowrampup),
            "-slowrampdown",
            str(slowrampdown),
            "-floor",
            str(floor),
            "-highpassfreq",
            str(highpassfreq),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    features = features or make_temp()

    ret = subprocess.call(
        [
            "fluid-noveltyfeature",
            "-source",
            str(source),
            "-features",
            str(features),
            "-algorithm",
            str(algorithm),
            "-kernelsize",
            str(kernelsize),
            str(kernelsize),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsettings[2]),
            str(fftsettings[2]),
            "-padding",
            str(padding),
            "-filtersize",
            str(filtersize),
            str(filtersize),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)


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
    check_source_exists(source)

    features = features or make_temp()

    fftsettings = fft_sanitise(fftsettings)
    fftsize = fft_format(fftsettings)

    ret = subprocess.call(
        [
            "fluid-onsetfeature",
            "-source",
            str(source),
            "-features",
            str(features),
            "-fftsettings",
            str(fftsettings[0]),
            str(fftsettings[1]),
            str(fftsize),
            str(fftsize),
            "-filtersize",
            str(filtersize),
            "-framedelta",
            str(framedelta),
            "-metric",
            str(metric),
            "-padding",
            str(padding),
            "-numchans",
            str(numchans),
            "-numframes",
            str(numframes),
            "-startchan",
            str(startchan),
            "-startframe",
            str(startframe),
        ]
    )

    handle_ret(ret)
    return FluidSingleOutput(features)

def audiotransport(
    sourcea: str | FluidSingleOutput,
    sourceb: str | FluidSingleOutput,
    numchansa: int = -1,
    numframesa: int = -1,
    startchana: int = 0,
    startframea: int = 0,
    numchansb: int = -1,
    numframesb: int = -1,
    startchanb: int = 0,
    startframeb: int = 0,
    destination: str = "",
    interpolation: float = 0.5,
    fftsettings: list[int, int, int] = [1024, -1, -1],
) -> FluidSingleOutput:

    cli, output = compute_cli_call('audiotransport', locals())

    ret = subprocess.call(cli)
    handle_ret(ret)

    return FluidSingleOutput(output)