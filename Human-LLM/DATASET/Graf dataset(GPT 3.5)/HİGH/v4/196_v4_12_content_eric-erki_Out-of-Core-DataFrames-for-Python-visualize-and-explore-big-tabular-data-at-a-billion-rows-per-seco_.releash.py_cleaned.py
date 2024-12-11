from releash import *
b1 = ReleaseTargetGitPush()
b2 = add_package("packages/vaex-b2", "vaex-b2")
b3 = VersionSource(b2, '{path}/vaex/b2/_version.py')
b4 = ReleaseTargetGitTagVersion(b5=b3, prefix='b2-v')
b2.b5 = b3
b2.version_targets.append(VersionTarget(b2, '{path}/vaex/b2/_version.py'))
b2.release_targets.append(b4)
b2.release_targets.append(ReleaseTargetSourceDist(b2))
b2.release_targets.append(ReleaseTargetCondaForge(b2, '../feedstocks/vaex-b2-feedstock'))
b6 = ['vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server', 'vaex-astro', 'vaex-ui', 'vaex-jupyter', 'vaex-distributed', 'vaex-arrow', 'vaex-ml']
for package_name in b6:
    b7 = package_name[5:]
    if b7 = = 'meta':
        b8 = add_package("packages/vaex-" + b7, "vaex-" + b7, 'vaex.' + b7, distribution_name='vaex')
        b9 = VersionSource(b8, '{path}/vaex/' + b7 + '/_version.py')
    elif b7 = = 'arrow':
        b8 = add_package("packages/vaex-" + b7, "vaex-" + b7, 'vaex_' + b7)
        b9 = VersionSource(b8, '{path}/vaex_' + b7 + '/_version.py')
    else:
        b8 = add_package("packages/vaex-" + b7, "vaex-" + b7, 'vaex.' + b7)
        b9 = VersionSource(b8, '{path}/vaex/' + b7 + '/_version.py')
    b10 = ReleaseTargetGitTagVersion(b5=b9, prefix=b7 + '-v', msg='Release {b9} of vaex-' + b7)
    b8.b5 = b9
    if b7 = = 'arrow':
        b8.version_targets.append(VersionTarget(b8, '{path}/vaex_' + b7 + '/_version.py'))
    else:
        b8.version_targets.append(VersionTarget(b8, '{path}/vaex/' + b7 + '/_version.py'))
    b8.release_targets.append(b10)
    b8.release_targets.append(ReleaseTargetSourceDist(b8))
    b8.release_targets.append(b1)
    if b7 = = 'meta':
        b8.release_targets.append(ReleaseTargetCondaForge(b8, '../feedstocks/vaex' + '-feedstock'))
    else:
        b8.release_targets.append(ReleaseTargetCondaForge(b8, '../feedstocks/vaex-' + b7 + '-feedstock'))