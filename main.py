from scripts.server import create_app
import sys, os,json
from pathlib import Path
from scripts import CANDIDATES,RESULTS_PATH,RAW_RESULT

from gui import GUI

path = Path(os.getcwd())
sys.path.append(path)

if __name__ == "__main__":
    res_path = RESULTS_PATH.resolve()
    if not os.path.exists(res_path/"results.json"):
        res_path.mkdir(parents=True,exist_ok=True)
        (res_path / "results.json").write_text(json.dumps(RAW_RESULT,indent=5))
    server = create_app()

    gui = GUI(server)
    gui.run()

