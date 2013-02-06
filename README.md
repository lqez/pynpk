pynpk - A python binding for npk
================================
[![Build Status](https://travis-ci.org/lqez/pynpk.png?branch=master)](https://travis-ci.org/lqez/pynpk)

- [npk](https://github.com/lqez/npk) is a simple package system for multiple files.
- Open, create and manipulate npk packages via python.
- Built on [cffi](http://pypi.python.org/pypi/cffi).

Installation
============

Before using pynpk, we need to get libnpk.

Get libnpk
----------
    $ git clone https://github.com/lqez/npk.git
    $ cd npk
    $ ./build.sh && cd _build && sudo make install

... or if you're on OS X and using Homebrew, then

    // NOT supported, yet :(
    $ brew install npk  
    
Get pynpk
---------
    $ pip install pynpk


Usage
=====

    import npk
    
    pack = npk.package("foo.npk")               # open package 
    entity = pack.get("bar.txt")                # find entity
    open('bar.txt','w').write(entity.read())    # write to file
    pack.export("bar.txt")                      # or just export it
    pack.close()                                # closing 

