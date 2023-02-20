import numpy as np
from dataclasses import dataclass
from flucoma.utils import get_buffer

@dataclass
class FlucomaSingleOutput:
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

	def get_data(self):
		return self.data

@dataclass
class HPSSOutput:
	harmonic_path: str = ''
	percussive_path: str = ''
	residual_path: str = ''

	def __post_init__(self):
		self.harmonic = FlucomaSingleOutput(self.harmonic_path)
		self.percussive = FlucomaSingleOutput(self.percussive_path)
		if self.residual_path != '':
			self.residual = FlucomaSingleOutput(self.residual_path)

class NMFOutput:
	resynth_path: str = ''
	bases_path: str = ''
	activations_path: str = ''

	def __post_init__(self):
		self.activations = FlucomaSingleOutput(self.activations_path)
		self.bases = FlucomaSingleOutput(self.bases_path)
		self.activations = FlucomaSingleOutput(self.activations_path)

class SinesOutput:
	sines_path: str = ''
	residual_path: str = ''

	def __post_init__(self):
		self.sines = FlucomaSingleOutput(self.sines_path)
		self.residual = FlucomaSingleOutput(self.residual_path)

class TransientsOutput:
	transients_path: str = ''
	residual_path: str = ''

	def __post_init__(self):
		self.transients = FlucomaSingleOutput(self.transients_path)
		self.residual = FlucomaSingleOutput(self.residual_path)