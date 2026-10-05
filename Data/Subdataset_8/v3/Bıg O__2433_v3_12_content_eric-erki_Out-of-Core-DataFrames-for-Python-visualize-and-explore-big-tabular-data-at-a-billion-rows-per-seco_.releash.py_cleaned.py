from releash import *
gitpush = ReleaseTargetGitPush()
def add_vaex_package(name, path_prefix='vaex', distribution_name=None):
    package_path = f"packages/{path_prefix}-{name}"
    full_name = f"vaex-{name}"
    import_name = full_name.replace('-', '_') if name != 'meta' else full_name
    package = add_package(package_path, full_name, import_name, distribution_name=distribution_name)
    return package
def add_vaex_version_source(package, name, import_name, path_prefix='vaex'):
    version_path = f"{path_prefix}/{name}/_version.py"
    return VersionSource(package, f"{{path}}/{version_path}")
package_names = ['core', 'meta', 'viz', 'hdf5', 'server', 'astro', 'ui', 'jupyter', 'distributed', 'arrow', 'ml']
for name in package_names:
    package = add_vaex_package(name)
    import_name = 'vaex.' + name if name != 'arrow' else 'vaex_' + name
    version_source = add_vaex_version_source(package, name, import_name)
    prefix = f"{name}-v" if name != 'arrow' else 'arrow-v'
    msg = f"Release {{version}} of vaex-{name}"
    gittag = ReleaseTargetGitTagVersion(version_source=version_source, prefix=prefix, msg=msg)
    package.version_source = version_source
    version_path = f"{name}" if name != 'arrow' else f"_{name}"
    package.version_targets.append(VersionTarget(package, f"{{path}}/vaex/{version_path}/_version.py"))
    package.release_targets.extend([gittag, ReleaseTargetSourceDist(package), gitpush])
    feedstock_name = 'feedstock' if name == 'meta' else f"vaex-{name}-feedstock"
    feedstock_path = '../feedstocks/' + feedstock_name
    package.release_targets.append(ReleaseTargetCondaForge(package, feedstock_path))