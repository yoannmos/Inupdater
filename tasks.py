import os
import webbrowser
from pathlib import Path
from shutil import copyfile, rmtree

from invoke import task


@task()
def clean(c):

    rmtree("build", ignore_errors=True)
    rmtree("dist", ignore_errors=True)
    rmtree(".pytest_cache", ignore_errors=True)
    rmtree("htmlcov", ignore_errors=True)
    rmtree("site", ignore_errors=True)
    rmtree("src/inupdater/__pycache__", ignore_errors=True)
    try:
        os.remove(".coverage")
    except:
        pass
    try:
        os.remove("coverage.xml")
    except:
        pass

    for item in os.listdir(Path().cwd()):
        if item.endswith(".spec"):
            os.remove(os.path.join(Path().cwd(), item))

    print("Your repo is clean !")


@task()
def test(c):
    c.run(
        "poetry run pytest --cov-report term --cov-report xml --cov=inupdater tests/ -vv"
    )


@task()
def docs(c):
    webbrowser.open("http://127.0.0.1:8000/")
    c.run("poetry run mkdocs serve")


@task(pre=[test])
def build(c):
    # TODO : try to get github ci
    c.run("poetry run pyside6-rcc resource.qrc -o src/inupdater/resource.py")
    c.run(
        "poetry run pyinstaller --clean --onefile --noconsole --name launcher --paths .venv/Lib/site-packages --exclude-module _bootlocale --paths .venv/Scripts src/inupdater/__main__.py"
    )
    print("Build SUCCESSFUL !")
