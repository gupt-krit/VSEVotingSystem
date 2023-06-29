import json,os
from pathlib import Path
path = Path(os.getcwd())
def load_imgs(post):
    img_path = path / "data" / "imgs"
    files = list(str(p) for p in img_path.glob(f'*_{post}.jpg'))
    return files
def load_json(path:str):
    file = open(path,'r')
    return json.load(file)