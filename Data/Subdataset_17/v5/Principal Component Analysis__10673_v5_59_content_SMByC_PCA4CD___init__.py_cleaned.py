
import os
import site
import pkg_resources
def add_extra_libs_to_path():
    current_directory = os.path.dirname(__file__)
    extra_libs_path = os.path.abspath(os.path.join(current_directory, "extlibs"))
    if os.path.isdir(extra_libs_path):
        site.addsitedir(extra_libs_path)
        pkg_resources.working_set.add_entry(extra_libs_path)
def classFactory(iface):
    add_extra_libs_to_path()
    from .pca4cd import PCA4CD
    return PCA4CD(iface)