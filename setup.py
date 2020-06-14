import setuptools
from pathlib import Path

readme = Path("./README.md").resolve()

with open(readme, encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="python-flucoma",
    version="1.0.1",
    author="James Bradbury",
    url="https://github.com/jamesb93/python-flucoma",
    author_email="jamesbradbury93@gmail.com",
    description="Loose bindings to the FluCoMa command line",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages=["flucoma"],
    install_requires=[
        "SoundFile",
        "numpy",
    ],
)
