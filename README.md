pynpk - A python binding for npk
================================

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
    
    # open package
    pack = npk.package("foo.npk")

    # find entity
    entity = pack.get("bar.txt")

    # write to file
    open('bar.txt','w').write(entity.read())

    # or just export it
    pack.export("bar.txt")

    # closing
    pack.close()

