
import os
import site
import pkg_resources
def add_extra_libs_to_path():
    extlibs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "extlibs"))
    if os.path.isdir(extlibs_path):
        site.addsitedir(extlibs_path)
        pkg_resources.working_set.add_entry(extlibs_path)
def classFactory(iface):
    add_extra_libs_to_path()
    from .pca4cd import PCA4CD
    return PCA4CD(iface)