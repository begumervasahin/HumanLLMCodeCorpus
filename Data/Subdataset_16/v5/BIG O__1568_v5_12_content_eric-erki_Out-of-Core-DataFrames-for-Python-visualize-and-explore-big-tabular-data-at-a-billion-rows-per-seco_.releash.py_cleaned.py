from releash import *
b1 = ReleaseTargetGitPush()
b2 = "b7/vaex-b3"
b3 = add_package(b2, "vaex-b3")
b4 = VersionSource(b3, f'{b2}/vaex/b3/_version.py')
b5 = ReleaseTargetGitTagVersion(b6=b4, prefix='b3-v')
b3.b6 = b4
b3.version_targets.append(VersionTarget(b3, f'{b2}/vaex/b3/_version.py'))
b3.release_targets.extend([
    b5,
    ReleaseTargetSourceDist(b3),
    ReleaseTargetCondaForge(b3, '../feedstocks/vaex-b3-feedstock')
])
b7 = [
    'vaex-b3', 'vaex-meta', 'vaex-viz', 'vaex-hdf5', 'vaex-server',
    'vaex-astro', 'vaex-ui', 'vaex-jupyter', 'vaex-distributed',
    'vaex-arrow', 'vaex-ml'
]
def fonk1(b12, b13, b14, b8 = None, b15=None):
    b9 = add_package(b13, b12, b14, b8=b8)
    b10 = VersionSource(b9, f'{b13}/{b14.replace(".", "/")}/_version.py')
    b11 = ReleaseTargetGitTagVersion(b6=b10, prefix=f'{b12}-v', msg=f'Release {{b10}} of {b12}')
    b9.b6 = b10
    b9.version_targets.append(VersionTarget(b9, f'{b13}/{b14.replace(".", "/")}/_version.py'))
    b9.release_targets.extend([
        b11,
        ReleaseTargetSourceDist(b9),
        b1,
        ReleaseTargetCondaForge(b9, f'../feedstocks/vaex{b15}-feedstock' if b15 else '../feedstocks/vaex-feedstock')
    ])
for full_name in b7[1:]:
    b12 = full_name[5:]
    b13 = f"b7/vaex-{b12}"
    b14 = f"vaex.{b12}" if b12 not in ['meta', 'arrow'] else f"vaex_{b12}" if b12 == 'arrow' else f"vaex.{b12}"
    b8 = 'vaex' if b12 == 'meta' else None
    b15 = '' if b12 == 'meta' else f'-{b12}'
    fonk1(f"vaex-{b12}", b13, b14, b8, b15)