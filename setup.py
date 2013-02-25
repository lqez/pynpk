from __future__ import with_statement
import os.path
import re
from setuptools import find_packages, setup
from setuptools.command.test import test
import sys

try:
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        requirements = [i for i in f if not i.startswith('#')]
except IOError:
    requirements = []

# use pytest instead
def run_tests(self):
    pyc = re.compile(r'\.pyc|\$py\.class')
    test_file = pyc.sub('.py', __import__(self.test_suite).__file__)
    raise SystemExit(__import__('pytest').main([test_file]))
test.run_tests = run_tests

tests_require = ['pytest']

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
    version='0.1.1',
    packages=['npk'],
    author='Park Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/pynpk',
    description='pynpk',
    install_requires=requirements,
    classifiers=classifiers,
    test_suite='npktest',
    tests_require=tests_require,
)
