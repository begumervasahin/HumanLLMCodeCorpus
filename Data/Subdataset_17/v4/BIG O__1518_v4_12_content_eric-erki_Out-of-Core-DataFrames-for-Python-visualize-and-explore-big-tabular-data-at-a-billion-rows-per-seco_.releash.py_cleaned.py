from releash import *
gitpush = ReleaseTargetGitPush()
core = add_package("packages/vaex-core", "vaex-core")
version_core = VersionSource(core, '{path}/vaex/core/_version.py')
gittag_core = ReleaseTargetGitTagVersion(version_source=version_core, prefix='core-v')
core.version_source = version_core
core.version_targets.append(VersionTarget(core, '{path}/vaex/core/_version.py'))
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
package_names = [pkg[5:] for pkg in packages[1:]]
for name in package_names:
    if name == 'meta':
        package = add_package(f"packages/vaex-{name}", f"vaex-{name}", f"vaex.{name}", distribution_name='vaex')
        version = VersionSource(package, f'{path}/vaex/{name}/_version.py')
    elif name == 'arrow':
        package = add_package(f"packages/vaex-{name}", f"vaex-{name}", f"vaex_{name}")
        version = VersionSource(package, f'{path}/vaex_{name}/_version.py')
    else:
        package = add_package(f"packages/vaex-{name}", f"vaex-{name}", f"vaex.{name}")
        version = VersionSource(package, f'{path}/vaex/{name}/_version.py')
    gittag = ReleaseTargetGitTagVersion(version_source=version, prefix=f'{name}-v', msg=f'Release {{version}} of vaex-{name}')
    package.version_source = version
    if name == 'arrow':
        package.version_targets.append(VersionTarget(package, f'{path}/vaex_{name}/_version.py'))
    else:
        package.version_targets.append(VersionTarget(package, f'{path}/vaex/{name}/_version.py'))
    package.release_targets.extend([
        gittag,
        ReleaseTargetSourceDist(package),
        gitpush
    ])
    if name == 'meta':
        package.release_targets.append(ReleaseTargetCondaForge(package, '../feedstocks/vaex-feedstock'))
    else:
        package.release_targets.append(ReleaseTargetCondaForge(package, f'../feedstocks/vaex-{name}-feedstock'))