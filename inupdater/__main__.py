import sys
import time
from pathlib import Path

from inupdater.ui import CmdUI, QtUI
from inupdater.updater import ExeUpdater

try:
    install_path = Path(sys.argv[-1]).parent
    user_interface = QtUI()
    updater = ExeUpdater(install_path, user_interface)
    updater.launch(Path.cwd())

except SystemExit as e:
    user_interface.show_message(
        "[ERROR] System Error !!! [This window will exit in 5s]"
    )
    print(e)
    time.sleep(5)

except FileNotFoundError as e:
    user_interface.show_message(
        "[ERROR] Your Setting File can't be found [This window will exit in 5s]"
    )
    print(e)
    time.sleep(5)
