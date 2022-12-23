from invoke import task
import platform

is_not_windows = bool(platform.system()!="Windows")

@task
def start(c):
    c.run("python src/main.py", pty=is_not_windows)

@task
def test(c):
    c.run("pytest src")

@task
def coverage(c):
    c.run("coverage run -m pytest src")
    c.run("coverage html")

@task
def format(c):
    c.run("black src")

@task
def lint(c):
    c.run("pylint src", pty=is_not_windows)

@task
def performance_test(c):
    c.run("python src/tests/performance_test.py", pty=is_not_windows)

@task
def build(c):
    c.run("pyinstaller --onefile -y --name MazeGen src/main.py")