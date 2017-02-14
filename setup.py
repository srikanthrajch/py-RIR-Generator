from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourcefiles = ["rir_generator.c", "rirgenerator.pyx"]
ext_modules = [Extension("rirgenerator", sourcefiles,libraries=['m'])]

setup(
	name = 'RIRGenerator',
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules
)
