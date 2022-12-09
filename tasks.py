from invoke import task

@task
def start(c):
    c.run("python src/main.py", pty=True)

@task
def test(c):
    c.run("pytest src", pty=True)

@task
def coverage(c):
    c.run("coverage run -m pytest src")
    c.run("coverage html")

@task
def format(c):
    c.run("black src")

@task
def lint(c):
    c.run("pylint src")

@task
def performance_test(c):
    c.run("python src/tests/performance_test.py", pty=True)

@task
def build(c):
    c.run("pyinstaller --onefile -y --name MazeGen src/main.py")