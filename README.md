# NLP Preprocessing Package

This is a text processing lirary. The library is divided into following modules.


<p> <b> Load Data </b>
<p> This module contains all the functions for loading the data and outputting results

<p> <b> Text Processing</b>
<p> This module contains the functions for tokenizing, normalising, removing special characters etc.

<p> <b> Feature Selection	</b>
<p> This module contains the functions for selecting text features like word frequency, ngrams, TTR etc.

<p> <b> Distance Measures	</b>
<p> This module contains the functions for calculating the distance and similarity between two vectors

<p> <b> Corpus Processor </b>
<p> This is a module which helps to convert the corpus into dictionaries (Key- Author, Values - Books by author)


## Building and Installation

#### Build package
Building requires <b> wheel </b>. If not installed, please install using the following command.

```python3 -m pip install --user --upgrade setuptools wheel```

Install requirements

```pip install -r requirements.txt```

Then enter the package directory and build the package using the following command.

```python3 setup.py sdist bdist_wheel```

This creates the dist folder containing the packaged tar files.

#### Install package

```pip install ./dist/preprocess_NLP_pkg-0.0.1.tar.gz```

#### To Uninstall package

```pip uninstall preprocess_NLP_pkg-0.0.1```