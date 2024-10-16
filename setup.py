"""The setup module to create the package to be distriubted on pypi"""
from setuptools import setup, find_packages
from pathlib import Path

VERSION = '1.1.1'
DESCRIPTION = 'Assetto Corsa intellisense stubs helper'
LONG_DESCRIPTION = Path('README.md').read_text(encoding='utf-8')

# Setting up
print(find_packages())
setup(
    name='acintellisense',
    version=VERSION,
    author='RipRock',
    author_email='<me@riprock.tech>',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
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
