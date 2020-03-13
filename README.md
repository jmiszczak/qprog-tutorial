# qprog-tutorial

Tutorial and code examples preapred for [QIPLSIGML meeting](https://qiplsigml.iitis.pl/), Machine Learning meets Quantum Computation. April 26-28, 2018, Kraków, Poland.

Subdirectory `slides` contains LaTeX files for producing beamer slides.

# Requirements

You will need
* Julia to run examples in `julia` subdirectory. They are run by simply including
  the files.
* Access to Wolfram Mathematica for running examples in `mma`. 
* Examples in `projectq` subdirectory are provided in Jupyter. You will need to
  install [ProjectQ](https://github.com/ProjectQ-Framework/ProjectQ) Python
library.
* For playing with QCL and running examples from `qcl` subdir, download the
  interpreter from [QCL web page](http://tph.tuwien.ac.at/~oemer/qcl.html).
* For running examples in `pyquil` subdir you will need
  [PyQuil](https://github.com/rigetticomputing/pyquil).

# Updates

* 03/03/2020 Added quantum mini-language in Python.
* 07/03/2019 Julia implementation of the Grover's algorithm updated for Julia 1.0. The basic example in pyQuil now runs on qvm.
* 06/03/2019 ProjectQ examples have been updated to take into account changes in backend usage and measurement syntax.
