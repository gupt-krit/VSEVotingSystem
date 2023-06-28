from scripts.server import create_app
import sys, os
from pathlib import Path

path = Path(os.getcwd())
sys.path.append(path)

if __name__ == "__main__":
    server = create_app()

    server.run(debug=True)
