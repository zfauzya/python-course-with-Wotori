import os
from pathlib import Path

# BASICS
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = str(Path(SETTINGS_DIR).parent.parent)
