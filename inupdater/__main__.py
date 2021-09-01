import sys
from pathlib import Path

from inupdater.updater import ExeUpdater

try:
    install_path = Path(sys.argv[-1]).parent
    updater = ExeUpdater(install_path)
    updater.launch(Path.cwd())

except SystemExit as e:
    print("Error!")
    print("Press enter to exit (and fix the problem)")
    input()
