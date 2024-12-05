### Installation instructions


* Install `pyenv` (https://github.com/pyenv/pyenv) and setup python 2.7.17 as `local` with `pyenv local 2.7.17` command
* Troubleshooting: In case of build failure follow these instructions: [Build Troubleshooting/FAQ](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
* Install `virtualenv` using `python2 -m pip install virtualenv` command
* Create `.venv` using `pyenv exec python -m virtualenv .venv` command
* Activate venv using `source .venv/bin/activate` 
* Make sure to install these libraries for JPEG headers with `sudo apt install libjpeg-dev zlib1g-dev` command
* Install requirements using `requirements.txt` file using `pip install -r requirements.txt` command
* Deactivate `venv` using `deactivate` command