from invoke import task

@task
def start(c):
    c.run("python src/index.py")