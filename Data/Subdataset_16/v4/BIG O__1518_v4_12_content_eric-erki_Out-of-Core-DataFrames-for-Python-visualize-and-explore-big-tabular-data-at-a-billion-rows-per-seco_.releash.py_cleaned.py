from releash import *
b1 = ReleaseTargetGitPush()
b2 = add_package("b6/vaex-b2", "vaex-b2")
b3 = VersionSource(b2, '{path}/vaex/b2/_version.py')
b4 = ReleaseTargetGitTagVersion(b5=b3, prefix='b2-v')
b2.b5 = b3
b2.version_targets.append(VersionTarget(b2, '{path}/vaex/b2/_version.py'))
b2.release_targets.extend([
    b4,
    ReleaseTargetSourceDist(b2),
    ReleaseTargetCondaForge(b2, '../feedstocks/vaex-b2-feedstock')
])
b6 = [
    'vaex-b2', 'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter', 'vaex-distributed',
    'vaex-arrow', 'vaex-ml'
]
b7 = [pkg[5:] for pkg in b6[1:]]
for b8 in b7:
    if b8 = = 'meta':
        b9 = add_package(f"b6/vaex-{b8}", f"vaex-{b8}", f"vaex.{b8}", distribution_name='vaex')
        b10 = VersionSource(b9, f'{path}/vaex/{b8}/_version.py')
    elif b8 = = 'arrow':
        b9 = add_package(f"b6/vaex-{b8}", f"vaex-{b8}", f"vaex_{b8}")
        b10 = VersionSource(b9, f'{path}/vaex_{b8}/_version.py')
    else:
        b9 = add_package(f"b6/vaex-{b8}", f"vaex-{b8}", f"vaex.{b8}")
        b10 = VersionSource(b9, f'{path}/vaex/{b8}/_version.py')
    b11 = ReleaseTargetGitTagVersion(b5=b10, prefix=f'{b8}-v', msg=f'Release {{b10}} of vaex-{b8}')
    b9.b5 = b10
    if b8 = = 'arrow':
        b9.version_targets.append(VersionTarget(b9, f'{path}/vaex_{b8}/_version.py'))
    else:
        b9.version_targets.append(VersionTarget(b9, f'{path}/vaex/{b8}/_version.py'))
    b9.release_targets.extend([
        b11,
        ReleaseTargetSourceDist(b9),
        b1
    ])
    if b8 = = 'meta':
        b9.release_targets.append(ReleaseTargetCondaForge(b9, '../feedstocks/vaex-feedstock'))
    else:
        b9.release_targets.append(ReleaseTargetCondaForge(b9, f'../feedstocks/vaex-{b8}-feedstock'))