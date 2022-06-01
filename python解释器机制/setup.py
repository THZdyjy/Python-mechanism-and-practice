from setuptools import setup, Extension

module = Extension('simple_add', sources=['simple_add.pyx'])

setup(
    name='cythonTest',
    version='1.0',
    author='jetbrains',
    ext_modules=[module]
)

