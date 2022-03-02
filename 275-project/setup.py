from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='Hello world app',
    ext_modules=cythonize("cyStdDev.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
