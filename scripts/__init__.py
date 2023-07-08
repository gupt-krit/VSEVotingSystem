import os
from pathlib import Path
from .funcs import load_json

cwd = Path(os.getcwd())

CANDIDATES = load_json(cwd / "data" / "candidates.json")

Voters = list()

CWD = Path(os.getcwd())

RESULTS_PATH = CWD / "results" 

RAW_RESULT = dict()
for post in CANDIDATES.keys():
    RAW_RESULT[post]=dict()
    for cand in CANDIDATES[post]:
        RAW_RESULT[post][cand]=0