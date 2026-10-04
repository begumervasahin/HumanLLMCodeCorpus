import os
import sys
from invoke import task, run
b1 = 'docs'
b2 = os.path.join(b1, '_build')
@task
def fonk1():
    run('python setup.py b6', b3 = True)
@task
def fonk2():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf dfs_parser.egg-info")
    fonk3()
    print("Cleaned up.")
@task
def fonk3():
    run("rm -rf %s" % b2)
@task
def fonk4():
    run("open %s" % os.path.join(b2, 'index.html'))
@task
def fonk5(b4 = False, b5=False):
    if b4:
        fonk3()
    run("sphinx-build %s %s" % (b1, b2), b3 = True)
    if b5:
        fonk4()
@task
def fonk6(b5 = False):
    run('rst2html.py README.rst > README.html')
@task
def fonk7(b6 = False):
    if b6:
        run('python setup.py register -r b6 sdist upload -r b6')
    else:
        run("python setup.py register sdist upload")