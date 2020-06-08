import setuptools

setuptools.setup(
    name="python-flucoma",
    version="0.1",
    author="James Bradbury",
    author_email="jamesbradbury93@gmail.com",
    description="Loose bindings to the FluCoMa command line",
    packages=["flucoma"],
    install_requires=[
        "SoundFile",
        "numpy",
    ],
)
