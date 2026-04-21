from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/app.py",pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage report")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")