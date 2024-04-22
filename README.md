# CrewAI - Getting Started

A few tests with Crew.AI platform based on [official docs](
https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/).


## Pre-reqs

### Python Virtual Environment
```
$ export VENVDIR=~/Code/test-crewai

$ python3 --version
Python 3.9.6

$ python3 -m venv $VENVDIR
$ cd $VENVDIR
$ ls 
README.md       bin             include         lib             pyvenv.cfg

$ source $VENVDIR/bin/activate
$ python --version
Python 3.9.6

$ python -m pip install --upgrade pip
Requirement already satisfied: pip in ./lib/python3.9/site-packages (21.2.4)
Collecting pip
  Downloading pip-24.0-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 833 kB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-24.0

$ pip --version
pip 24.0 from /Users/alastori/Code/test-crewai/lib/python3.9/site-packages/pip (python 3.9)
```
