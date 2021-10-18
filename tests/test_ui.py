import pytest

from inupdater.ui import CmdUI, QtUI


def ui_TESTING():
    """TODO : Unit testing those"""
    app_name = "My APP"
    version = "1.1"

    uis = [CmdUI(), QtUI()]

    messages = [
        "Checking for updates...",
        f"We find a new update ! {app_name}_{version}",
        f"Downloading {app_name}_{version}...",
        "Update downloaded !",
        f"Installing {app_name}_{version}...",
        "Update installed !",
        f"Launching {app_name}_{version}...",
        "Please wait...",
    ]

    for ui in uis:
        for idx, msg in enumerate(messages):
            ui.show_message(msg)
            ui.set_state(int((idx + 1) / 0.7))


if __name__ == "__main__":
    ui_TESTING()
