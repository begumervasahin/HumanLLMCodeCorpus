from releash import *
gitpush = ReleaseTargetGitPush()
core_package = "packages/vaex-core"
core = add_package(core_package, "vaex-core")
version_core = VersionSource(core, f'{core_package}/vaex/core/_version.py')
gittag_core = ReleaseTargetGitTagVersion(version_source=version_core, prefix='core-v')
core.version_source = version_core
core.version_targets.append(VersionTarget(core, f'{core_package}/vaex/core/_version.py'))
core.release_targets.extend([
    gittag_core,
    ReleaseTargetSourceDist(core),
    ReleaseTargetCondaForge(core, '../feedstocks/vaex-core-feedstock')
])
packages = [
    'vaex-core', 'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter', 'vaex-distributed',
    'vaex-arrow', 'vaex-ml'
]
def setup_package(name, path, module_name, distribution_name=None, conda_suffix=None):
    package = add_package(path, name, module_name, distribution_name=distribution_name)
    version = VersionSource(package, f'{path}/{module_name.replace(".", "/")}/_version.py')
    gittag = ReleaseTargetGitTagVersion(version_source=version, prefix=f'{name}-v', msg=f'Release {{version}} of {name}')
    package.version_source = version
    package.version_targets.append(VersionTarget(package, f'{path}/{module_name.replace(".", "/")}/_version.py'))
    package.release_targets.extend([
        gittag,
        ReleaseTargetSourceDist(package),
        gitpush,
        ReleaseTargetCondaForge(package, f'../feedstocks/vaex{conda_suffix}-feedstock' if conda_suffix else '../feedstocks/vaex-feedstock')
    ])
for full_name in packages[1:]:
    name = full_name[5:]
    path = f"packages/vaex-{name}"
    module_name = f"vaex.{name}" if name not in ['meta', 'arrow'] else f"vaex_{name}" if name == 'arrow' else f"vaex.{name}"
    distribution_name = 'vaex' if name == 'meta' else None
    conda_suffix = '' if name == 'meta' else f'-{name}'
    setup_package(f"vaex-{name}", path, module_name, distribution_name, conda_suffix)