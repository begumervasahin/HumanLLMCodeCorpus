from releash import *
b1 = ReleaseTargetGitPush()
def fonk1(name, b2 = 'vaex', distribution_name=None):
    b3 = f"packages/{b2}-{name}"
    b4 = f"vaex-{name}"
    b5 = b4.replace('-', '_') if name != 'meta' else b4
    b6 = add_package(b3, b4, b5, distribution_name=distribution_name)
    return b6
def fonk2(b6, name, b5, b2 = 'vaex'):
    b7 = f"{b2}/{name}/_version.py"
    return VersionSource(b6, f"{{path}}/{b7}")
b8 = ['core', 'meta', 'viz', 'hdf5', 'server', 'astro', 'ui', 'jupyter', 'distributed', 'arrow', 'ml']
for name in b8:
    b6 = fonk1(name)
    b5 = 'vaex.' + name if name != 'arrow' else 'vaex_' + name
    b9 = fonk2(b6, name, b5)
    b10 = f"{name}-v" if name != 'arrow' else 'arrow-v'
    b11 = f"Release {{version}} of vaex-{name}"
    b12 = ReleaseTargetGitTagVersion(b9=b9, b10=b10, b11=b11)
    b6.b9 = b9
    b7 = f"{name}" if name != 'arrow' else f"_{name}"
    b6.version_targets.append(VersionTarget(b6, f"{{path}}/vaex/{b7}/_version.py"))
    b6.release_targets.extend([b12, ReleaseTargetSourceDist(b6), b1])
    b13 = 'feedstock' if name == 'meta' else f"vaex-{name}-feedstock"
    b14 = '../feedstocks/' + b13
    b6.release_targets.append(ReleaseTargetCondaForge(b6, b14))