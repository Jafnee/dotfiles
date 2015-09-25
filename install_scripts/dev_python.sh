#!/usr/bin/env bash

apt-get install python-pip

mkdir -p $HOME/Envs
pip install virtualenv virtualenvwrapper
#just assume config has been handled in .bashrc