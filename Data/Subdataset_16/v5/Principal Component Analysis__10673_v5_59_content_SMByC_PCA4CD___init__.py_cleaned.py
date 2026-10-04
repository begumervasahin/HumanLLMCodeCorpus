
import os
import site
import pkg_resources
def fonk1():
    b1 = os.path.dirname(__file__)
    b2 = os.path.abspath(os.path.join(b1, "extlibs"))
    if os.path.isdir(b2):
        site.addsitedir(b2)
        pkg_resources.working_set.add_entry(b2)
def fonk2(iface):
    fonk1()
    from .pca4cd import PCA4CD
    return PCA4CD(iface)