#!/bin/sh

# install libnpk
git clone https://github.com/lqez/npk.git _libnpk
cd _libnpk
./build.sh && cd _build && sudo make install
cd ../..

# test pynpk
python setup.py test
