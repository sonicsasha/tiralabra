from invoke import task

@task
def start(c):
    c.run("python src/index.py")

@task
def test(c):
    c.run("pytest src", pty=True)

@task
def coverage(c):
    c.run("coverage run -m pytest src")
    c.run("coverage html")