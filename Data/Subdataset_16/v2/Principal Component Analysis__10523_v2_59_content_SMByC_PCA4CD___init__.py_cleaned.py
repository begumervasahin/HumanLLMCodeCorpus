
import os
import site
import pkg_resources
def fonk1():
    b1 = os.path.abspath(os.path.join(os.path.dirname(__file__), "extlibs"))
    if os.path.isdir(b1):
        site.addsitedir(b1)
        pkg_resources.working_set.add_entry(b1)
def fonk2(iface):
    fonk1()
    from .pca4cd import PCA4CD
    return PCA4CD(iface)