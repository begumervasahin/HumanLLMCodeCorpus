import os
from invoke import task, run
b1 = 'docs'
b2 = os.path.join(b1, '_build')
@task
def fonk1(c):
    run('python setup.py b7', b3 = True)
@task
def fonk2(c):
    run("rm -rf build dist dfs_parser.egg-info")
    fonk3(c)
    print("Cleaned up.")
@task
def fonk3(c):
    run(f"rm -rf {b2}")
@task
def fonk4(c):
    b4 = os.path.join(b2, 'index.html')
    run(f"open {b4}")
@task
def fonk5(c, b5 = False, b6=False):
    if b5:
        fonk3(c)
    run(f"sphinx-build {b1} {b2}", b3 = True)
    if b6:
        fonk4(c)
@task
def fonk6(c, b6 = False):
    run('rst2html.py README.rst > README.html')
    if b6:
        run("open README.html")
@task
def fonk7(c, b7 = False):
    b8 = 'b7' if b7 else ''
    run(f'python setup.py register -r {b8} sdist upload -r {b8}')