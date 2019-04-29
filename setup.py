import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lda",
    version="0.0.1",
    author="Yizi Lin, Siqi Fu",
    author_email="yizi.lin@duke.edu",
    description="Latent Dirichlet Allocation Model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyz1206/lda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
