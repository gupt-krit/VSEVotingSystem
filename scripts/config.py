import os,sys
from pathlib import Path
from .funcs import load_json
cwd = Path(os.getcwd())
class DataStore:
    CANDIDATE_LIST = load_json(cwd / "data" / "candidates.json")
    Voters = list()