from releash import *
b1 = ReleaseTargetGitPush()
def fonk1(package_name, b2 = 'vaex-', b5=None):
    b3 = package_name[5:]
    b4 = f"packages/{b2}{b3}"
    b5 = b5 if b5 else package_name
    b6 = add_package(b4, package_name, f"vaex.{b3}", b5=b5)
    b7 = '{b4}/vaex_' + b3 + '/_version.py' if b3 == 'arrow' else '{b4}/vaex/' + b3 + '/_version.py'
    b8 = VersionSource(b6, b7)
    b6.b9 = b8
    b10 = b7 if b3 == 'arrow' else '{b4}/vaex/' + b3 + '/_version.py'
    b6.version_targets.append(VersionTarget(b6, b10))
    b11 = ReleaseTargetGitTagVersion(b9=b8, prefix=b3 + '-v', msg=f'Release {{b8}} of {b5}')
    b6.release_targets.extend([b11, ReleaseTargetSourceDist(b6), b1])
    if b3 = = 'meta':
        b12 = 'vaex' + '-feedstock'
    else:
        b12 = f'vaex-{b3}-feedstock'
    b6.release_targets.append(ReleaseTargetCondaForge(b6, f'../feedstocks/{b12}'))
    return b6
b13 = fonk1('vaex-b13', 'vaex-b13')
b14 = ['vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server', 'vaex-astro', 'vaex-ui', 'vaex-jupyter', 'vaex-distributed', 'vaex-arrow', 'vaex-ml']
for package_name in b14:
    fonk1(package_name)