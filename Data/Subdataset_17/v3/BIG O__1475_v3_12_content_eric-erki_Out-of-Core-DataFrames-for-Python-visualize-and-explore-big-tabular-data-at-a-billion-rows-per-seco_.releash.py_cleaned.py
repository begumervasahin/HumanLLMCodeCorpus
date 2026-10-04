from releash import *
git_push_target = ReleaseTargetGitPush()
vaex_core = add_package("packages/vaex-core", "vaex-core")
core_version_path = '{path}/vaex/core/_version.py'
core_version_source = VersionSource(vaex_core, core_version_path)
core_git_tag = ReleaseTargetGitTagVersion(version_source=core_version_source, prefix='core-v')
vaex_core.version_source = core_version_source
vaex_core.version_targets.append(VersionTarget(vaex_core, core_version_path))
vaex_core.release_targets.extend([
    core_git_tag,
    ReleaseTargetSourceDist(vaex_core),
    ReleaseTargetCondaForge(vaex_core, '../feedstocks/vaex-core-feedstock')
])
package_names = [
    'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter',
    'vaex-distributed', 'vaex-arrow', 'vaex-ml'
]
def configure_package(name, package_path, version_path, is_meta=False, is_arrow=False):
    package = add_package(package_path, name, version_path, distribution_name='vaex' if is_meta else None)
    version_source = VersionSource(package, version_path)
    git_tag = ReleaseTargetGitTagVersion(version_source=version_source, prefix=f'{name}-v', msg=f'Release {{version}} of {name}')
    package.version_source = version_source
    package.version_targets.append(VersionTarget(package, version_path))
    conda_forge_path = '../feedstocks/vaex-feedstock' if is_meta else f'../feedstocks/{name}-feedstock'
    package.release_targets.extend([
        git_tag,
        ReleaseTargetSourceDist(package),
        git_push_target,
        ReleaseTargetCondaForge(package, conda_forge_path)
    ])
for name in package_names:
    if name == 'vaex-meta':
        configure_package(name, f'packages/{name}', '{path}/vaex/meta/_version.py', is_meta=True)
    elif name == 'vaex-arrow':
        configure_package(name, f'packages/{name}', '{path}/vaex_arrow/_version.py', is_arrow=True)
    else:
        configure_package(name, f'packages/{name}', f'{path}/vaex/{name[5:]}/_version.py')