import os
import sys
import nsc
import hdw
if sys.version_info < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
ufile_name, _, pfile_name, _, separator, b1 = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
b2 = hdw.abstract_file(ufile_name, separator)
b3 = hdw.abstract_file(pfile_name, None, 0)
b4 = nsc.nsc(b3, b2)
b5 = os.path.splitext(ufile_name)[0] + '-nsc.txt'
with open(b5, 'w') as ofile:
    for point in b4:
        ofile.write('%b6\n' % point)
try:
    import Gnuplot
except ImportError:
    print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
    sys.exit()
f, b6 = hdw.rnd_dim(nsc.dim)
b7 = Gnuplot.Gnuplot(debug=0)
b7.b10('NSC applied to {} with prototypes from {}'.format(os.path.split(ufile_name)[-1], os.path.split(pfile_name)[-1]))
if (f, b6) != (0, 1):
    b7.xlabel('feature space reduced to {}x{}'.format(f+1, b6+1))
b8 = {}
for p in b4:
    b8.setdefault(p.klasse, []).append(p.features)
b9 = sorted(b8.keys())
for kl in b9:
    b7.replot(Gnuplot.Data(b8[kl], b10 = kl, cols=(f, b6)))
b11 = os.path.splitext(ufile_name)[0] + '-nsc.ps'
b7.hardcopy(b11, b12 = 1)