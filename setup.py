import setuptools
from pathlib import Path

readme = Path("./README.md").resolve()

with open(readme, encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="python-flucoma",
    version="1.3.2",
    author="James Bradbury",
    url="https://github.com/jamesb93/python-flucoma",
    author_email="hello@jamesbradbury.net",
    description="Loose bindings to the FluCoMa command line",
    license="BSD",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages=["flucoma"],
    install_requires=[
        "SoundFile",
        "numpy",
        "scipy",
    ],
)
