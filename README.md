# CrewAI - Getting Started

A few tests with Crew.AI platform based on [official docs](
https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/).

Some tips collected from [Matthew Berman](https://www.youtube.com/watch?v=iJjSjmZnNlI).


## Pre-reqs

CrewAI is compatible with Python >=3.10,<=3.13.

[Latest stable Python](https://www.python.org/downloads/) for macOS is 3.12.3.

### Python 3.12
```
% brew install python@3.12
```
```
% /opt/homebrew/bin/python3 --version
Python 3.12.3
```

### Python Virtual Environment
```
% export VENVDIR=~/Code/test-crewai

% /opt/homebrew/bin/python3 -m venv $VENVDIR

% cd $VENVDIR
% ls 
README.md       bin             include         lib             pyvenv.cfg

% source $VENVDIR/bin/activate
(test-crewai) % python --version
Python 3.12.3

(test-crewai) % python -m pip install --upgrade pip
Requirement already satisfied: pip in ./lib/python3.12/site-packages (24.0)

(test-crewai) % pip --version
pip 24.0 from /Users/alastori/Code/test-crewai/lib/python3.12/site-packages/pip (python 3.12)
```

### File .gitignore
Create a `.gitignore` similar to one in this repo.

### Serper Key (Google Search API)
Go to [Seper website](https://serper.dev/), and get the API key.

### OpenAI Key
Go to [OpenAI](https://platform.openai.com/settings/profile?tab=api-keys) wesite, create the API key.

### File .env
Create `~\env\.env` file with environment variables:
```
SERPER_API_KEY=
OPENAI_API_KEY=
```


## Install CrewAI
```
(test-crewai) % pip install crewai
(test-crewai) % pip install 'crewai[tools]'
```

## Agents, Tasks, Crew, Run!
As seen in this repo:
- `~/technology_research_crew/research_cloud_databases_market_segments.py`
- `~/technology_research_crew/research_ai_in_healthcare.py`
