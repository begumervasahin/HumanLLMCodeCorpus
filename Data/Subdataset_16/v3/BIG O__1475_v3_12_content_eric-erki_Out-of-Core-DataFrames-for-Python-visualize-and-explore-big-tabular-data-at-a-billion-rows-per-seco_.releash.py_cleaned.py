from releash import *
b1 = ReleaseTargetGitPush()
b2 = add_package("packages/vaex-core", "vaex-core")
b3 = '{path}/vaex/core/_version.py'
b4 = VersionSource(b2, b3)
b5 = ReleaseTargetGitTagVersion(b6=b4, prefix='core-v')
b2.b6 = b4
b2.version_targets.append(VersionTarget(b2, b3))
b2.release_targets.extend([
    b5,
    ReleaseTargetSourceDist(b2),
    ReleaseTargetCondaForge(b2, '../feedstocks/vaex-core-feedstock')
])
b7 = [
    'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter',
    'vaex-distributed', 'vaex-arrow', 'vaex-ml'
]
def fonk1(b12, package_path, version_path, b8 = False, b13=False):
    b9 = add_package(package_path, b12, version_path, distribution_name='vaex' if b8 else None)
    b6 = VersionSource(b9, version_path)
    b10 = ReleaseTargetGitTagVersion(b6=b6, prefix=f'{b12}-v', msg=f'Release {{version}} of {b12}')
    b9.b6 = b6
    b9.version_targets.append(VersionTarget(b9, version_path))
    b11 = '../feedstocks/vaex-feedstock' if b8 else f'../feedstocks/{b12}-feedstock'
    b9.release_targets.extend([
        b10,
        ReleaseTargetSourceDist(b9),
        b1,
        ReleaseTargetCondaForge(b9, b11)
    ])
for b12 in b7:
    if b12 = = 'vaex-meta':
        fonk1(b12, f'packages/{b12}', '{path}/vaex/meta/_version.py', b8 = True)
    elif b12 = = 'vaex-arrow':
        fonk1(b12, f'packages/{b12}', '{path}/vaex_arrow/_version.py', b13 = True)
    else:
        fonk1(b12, f'packages/{b12}', f'{path}/vaex/{b12[5:]}/_version.py')