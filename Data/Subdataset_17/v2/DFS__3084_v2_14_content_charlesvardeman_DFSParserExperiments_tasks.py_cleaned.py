import os
from invoke import task, run
docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')
@task
def test(c):
    run('python setup.py test', pty=True)
@task
def clean(c):
    run("rm -rf build dist dfs_parser.egg-info")
    clean_docs(c)
    print("Cleaned up.")
@task
def clean_docs(c):
    run(f"rm -rf {build_dir}")
@task
def browse_docs(c):
    index_path = os.path.join(build_dir, 'index.html')
    run(f"open {index_path}")
@task
def build_docs(c, clean=False, browse=False):
    if clean:
        clean_docs(c)
    run(f"sphinx-build {docs_dir} {build_dir}", pty=True)
    if browse:
        browse_docs(c)
@task
def readme(c, browse=False):
    run('rst2html.py README.rst > README.html')
    if browse:
        run("open README.html")
@task
def publish(c, test=False):
    if test:
        run('python setup.py register -r test sdist upload -r test')
    else:
        run("python setup.py register sdist upload")