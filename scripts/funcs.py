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
def split_list(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]
def save_response(response:dict,posts,path):
    from . import RAW_RESULT

    try:
        standings = json.load(open(path,'r'))
    except json.decoder.JSONDecodeError:
        json.dump(RAW_RESULT,open(path,'w'),indent=5)
        standings=json.load(open(path,'r'))
    for post in posts:
        if post in response:
            for cand in standings[post].keys():
                if cand == response[post]:
                    standings[post][cand]+=1
        else:
            continue

    file_ = open(path,'w')
    json.dump(standings,file_,indent=5)