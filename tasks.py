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
def test(c, cov=None):
    rmtree(".pytest_cache", ignore_errors=True)
    try:
        os.remove(".coverage")
    except FileNotFoundError:
        pass
    c.run("poetry run coverage run -m pytest")
    if cov:
        try:
            os.remove("coverage.xml")
        except:
            pass
        rmtree("htmlcov", ignore_errors=True)

        c.run("poetry run coverage html")
        site = "file://" + str(Path("htmlcov/index.html").absolute())
        webbrowser.open(site)

    else:
        c.run("poetry run coverage run -m pytest")


@task()
def docs(c):
    webbrowser.open("http://127.0.0.1:8000/")
    c.run("poetry run mkdocs serve")


@task(pre=[clean, test])
def build(c):

    c.run(
        "pyinstaller --clean --onefile --name launcher --paths .venv/Lib/site-packages --paths .venv/Scripts src/inupdater/__main__.py"
    )
    print("Build SUCCESSFUL !")
