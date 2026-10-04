
import os
import site
import pkg_resources
def pre_init_plugin_libs_inside():
    extra_libs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "extlibs"))
    if os.path.isdir(extra_libs_path):
        site.addsitedir(extra_libs_path)
        pkg_resources.working_set.add_entry(extra_libs_path)
def classFactory(iface):
    pre_init_plugin_libs_inside()
    from .pca4cd import PCA4CD
    return PCA4CD(iface)