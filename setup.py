import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="preprocess_NLP_pkg",
    version="0.0.1",
    author="Sukanya Nath",
    author_email="8sukanya8@gmail.com",
    description="A small loading package for handling reading, preprocessing and outputting text data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)