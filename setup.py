#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA
import os.path

try:
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        requirements = [i for i in f if not i.startswith('#')]
except IOError:
    requirements = []

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='pynpk',
    version='0.1.0',
    py_modules=['pynpk'],
    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/pynpk',
    description='pynpk',
    install_requires=requirements,
    classifiers=classifiers,
)
