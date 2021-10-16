#!/bin/bash

set -x

PYTHON_VERSION=$(python3 --version)

if [[ "Python 3.8.2" == *"3.8.2"* ]]; then
   echo "Installing python dependencies.."

   pip install virtualenv
   python3 -m pip install pyqt5
   python3 -m venv smcsb-env
   python3 -m pip install soundfile
   python3 -m pip install sounddevice
   source ~/smcsb-env/bin/activate
   smcsb-env/bin/pip install google-cloud-speech
fi
