#!/bin/sh

# install libnpk
git clone https://github.com/lqez/npk.git _libnpk
cd "_libnpk"
mkdir "_build"
cd "_build"
cmake .. -DDEV_MODE=True -DBUILD_NPK=False
make && make test && sudo make install
cd ../..

# test pynpk
python setup.py test
