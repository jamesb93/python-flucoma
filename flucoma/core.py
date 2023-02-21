from dataclasses import dataclass
from flucoma.utils import get_buffer


@dataclass
class FluidSingleOutput:
    file_path: str

    def __post_init__(self):
        self.data = get_buffer(self.file_path, "numpy")

    def __str__(self):
        return self.file_path

    def __fspath__(self):
        return self.file_path

    def __iter__(self):
        for channel in self.data:
            yield channel

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


@dataclass
class FluidMultiOutput:
    def __iter__(self):
        for out in self.outputs:
            yield out

    def __len__(self):
        return len(self.outputs)

    def __getitem__(self, index):
        return self.outputs[index]


@dataclass
class HPSSOutput(FluidMultiOutput):
    harmonic_path: str
    percussive_path: str
    residual_path: str = ""

    def __post_init__(self):
        self.harmonic = FluidSingleOutput(self.harmonic_path) if self.harmonic_path else None
        self.percussive = FluidSingleOutput(self.percussive_path) if self.percussive_path else None
        self.residual = FluidSingleOutput(self.residual_path) if self.residual_path else None
        self.outputs = [out for out in [self.harmonic, self.percussive, self.residual] if out]


@dataclass
class NMFOutput(FluidMultiOutput):
    resynth_path: str = ""
    bases_path: str = ""
    activations_path: str = ""

    def __post_init__(self):
        self.resynth = FluidSingleOutput(self.resynth_path) if self.resynth_path else None
        self.bases = FluidSingleOutput(self.bases_path) if self.bases_path else None
        self.activations = (
            FluidSingleOutput(self.activations_path) if self.activations_path else None
        )
        self.outputs = [out for out in [self.resynth, self.bases, self.activations] if out]


@dataclass
class SinesOutput(FluidMultiOutput):
    sines_path: str = ""
    residual_path: str = ""

    def __post_init__(self):
        self.sines = FluidSingleOutput(self.sines_path) if self.sines_path else None
        self.residual = FluidSingleOutput(self.residual_path) if self.residual_path else None
        self.outputs = [out for out in [self.sines, self.residual] if out]


@dataclass
class TransientsOutput(FluidMultiOutput):
    transients_path: str = ""
    residual_path: str = ""

    def __post_init__(self):
        self.transients = FluidSingleOutput(self.transients_path) if self.transients_path else None
        self.residual = FluidSingleOutput(self.residual_path) if self.residual_path else None
        self.outputs = [out for out in [self.transients, self.residual] if out]
