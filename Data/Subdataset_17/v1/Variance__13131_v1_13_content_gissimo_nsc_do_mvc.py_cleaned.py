import os
import sys
import nsc
import hdw
from sets import Set as set, ImmutableSet as frozenset
if sys.version_info[:2] < (2, 4):
    print("Python version 2.4 or greater is required.")
    sys.exit()
ifile_name, sigma, _, _, separator, klasse_index = hdw.handle_commands(sys.argv, 's:', ['separator=', 'classid='])
universe = hdw.abstract_file(ifile_name, separator, klasse_index)
hdw.fill_world(universe)
prototypes = {}
for kl in nsc.welt.keys():
    nsc.computeRLs(kl)
    for pr in nsc.mvc(kl, sigma):
        if kl not in prototypes:
            prototypes[kl] = set()
        if not pr.isVoid():
            prototypes[kl].add(pr.mean)
ofile_name = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.txt"
with open(ofile_name, 'w') as ofile:
    for kl, points in prototypes.items():
        for point in points:
            ofile.write(f"{point}\n")
try:
    import Gnuplot
except ImportError:
    print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
    sys.exit()
f, s = hdw.rnd_dim(nsc.dim)
g = Gnuplot.Gnuplot(debug=0)
g.title(f'MVC applied to {os.path.basename(ifile_name)} with sigma^2={sigma:.4f}')
if (f, s) != (0, 1):
    g.xlabel(f'feature space reduced to {f+1}x{s+1}')
for kl in sorted(prototypes.keys()):
    if len(prototypes[kl]) == 0:
        continue
    l = [cen.features for cen in prototypes[kl]]
    prototypes[kl] = l
    g.replot(Gnuplot.Data(prototypes[kl], title=f'** {kl} **', cols=(f, s)))
for kl in sorted(nsc.welt.keys()):
    l = [p.features for p in nsc.welt[kl]]
    nsc.welt[kl] = l
    g.replot(Gnuplot.Data(nsc.welt[kl], title=kl, cols=(f, s)))
gfile_name = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.ps"
g.hardcopy(gfile_name, color=1)