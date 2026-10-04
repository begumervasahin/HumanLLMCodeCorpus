from releash import *
b1 = ReleaseTargetGitPush()
b2 = add_package("packages/vaex-core", "vaex-core")
b3 = VersionSource(b2, '{path}/vaex/core/_version.py')
b4 = ReleaseTargetGitTagVersion(b5=b3, prefix='core-v')
b2.b5 = b3
b2.version_targets.append(VersionTarget(b2, '{path}/vaex/core/_version.py'))
b2.release_targets.extend([
    b4,
    ReleaseTargetSourceDist(b2),
    ReleaseTargetCondaForge(b2, '../feedstocks/vaex-core-feedstock')
])
b6 = [
    'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter',
    'vaex-distributed', 'vaex-arrow', 'vaex-ml'
]
def fonk1(b10, package_path, version_path, b7 = False, b11=False):
    b8 = add_package(package_path, b10, version_path, distribution_name='vaex' if b7 else None)
    b5 = VersionSource(b8, version_path)
    b9 = ReleaseTargetGitTagVersion(b5=b5, prefix=f'{b10}-v', msg=f'Release {{version}} of {b10}')
    b8.b5 = b5
    b8.version_targets.append(VersionTarget(b8, version_path))
    b8.release_targets.extend([
        b9,
        ReleaseTargetSourceDist(b8),
        b1,
        ReleaseTargetCondaForge(b8, f'../feedstocks/{b10}-feedstock' if not b7 else '../feedstocks/vaex-feedstock')
    ])
for b10 in b6:
    if b10 = = 'vaex-meta':
        fonk1(b10, f'packages/{b10}', '{path}/vaex/meta/_version.py', b7 = True)
    elif b10 = = 'vaex-arrow':
        fonk1(b10, f'packages/{b10}', '{path}/vaex_arrow/_version.py', b11 = True)
    else:
        fonk1(b10, f'packages/{b10}', f'{path}/vaex/{b10[5:]}/_version.py')