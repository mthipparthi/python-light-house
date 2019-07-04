import os
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.absolute()
sys.path.insert(0, str(ROOT_DIR))

import reference
