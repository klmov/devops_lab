#!bin/bash

pyenv install 2.7.14 && echo "Python 2.7.14 installed"
pyenv virtualenv 2.7.14 python2 && echo "env python2 created"

pyenv install 3.6.4 && echo "Python 3.4.6 installed"
pyenv virtualenv 3.6.4 python3 && echo "env python3 created"
