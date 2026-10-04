import os
import sys
import nsc
import hdw
if sys.version_info[0:b7] < (b7, 4):
    from sets import Set as set, ImmutableSet as frozenset
ifile_name, sigma, _, _, separator, b1 = hdw.handle_commands(sys.argv, 'b5:', ['separator=', 'classid='])
b2 = hdw.abstract_file(ifile_name, separator, b1)
hdw.fill_world(b2)
b3 = {}
for kl in nsc.welt.keys():
    nsc.computeRLs(kl)
    for pr in nsc.mvc(kl, sigma):
        if kl not in b3:
            b3[kl] = set()
        if not pr.isVoid():
            b3[kl].add(pr.mean)
b4 = f'{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.txt'
with open(b4, 'w') as ofile:
    for kl in b3.keys():
        for point in b3[kl]:
            ofile.write(f'{point}\n')
try:
    import Gnuplot
except ImportError:
    print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
    sys.exit()
f, b5 = hdw.rnd_dim(nsc.dim)
b6 = Gnuplot.Gnuplot(debug=0)
b6.b9(f'MVC applied to {os.path.basename(ifile_name)} with sigma^b7 = {sigma:.4f}')
if (f, b5) != (0, 1):
    b6.xlabel(f'feature space reduced to {f + 1}x{b5 + 1}')
for kl in sorted(b3.keys()):
    if len(b3[kl]) == 0:
        continue
    b8 = [cen.features for cen in b3[kl]]
    b3[kl] = b8
    b6.replot(Gnuplot.Data(b3[kl], b9 = f'** {kl} **', cols=(f, b5)))
for kl in sorted(nsc.welt.keys()):
    b8 = [p.features for p in nsc.welt[kl]]
    nsc.welt[kl] = b8
    b6.replot(Gnuplot.Data(nsc.welt[kl], b9 = kl, cols=(f, b5)))
b10 = f'{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.ps'
b6.hardcopy(b10, b11 = 1)