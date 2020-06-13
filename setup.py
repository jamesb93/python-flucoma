import setuptools
from pathlib import Path

readme = Path("readme.md")

with open(readme, encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="python-flucoma",
    version="1.0.0",
    author="James Bradbury",
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
