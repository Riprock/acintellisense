"""The setup module to create the package to be distriubted on pypi"""
from setuptools import setup, find_packages

VERSION = '1.0.3'
DESCRIPTION = 'Assetto Corsa intellisense stubs helper'
LONG_DESCRIPTION = """Assetto Corsa stubs library for "ac" object. 
Helping intellisense and documentation when developing.

Currently only implemented whats in the known AC PDF for modding. Working on expanding in the future
"""
# Setting up
setup(
    name='acintellisense',
    version=VERSION,
    author='RipRock',
    author_email='<me@riprock.tech>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'AC', 'Assetto Corsa', 'dummy', 'stub'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Games/Entertainment :: Simulation',
    ]
)
