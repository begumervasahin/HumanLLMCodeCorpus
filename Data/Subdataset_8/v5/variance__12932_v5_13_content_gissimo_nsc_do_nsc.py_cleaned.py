import os
import sys
import nsc
import hdw
if sys.version_info < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
ufile_name, _, pfile_name, _, separator, klasse_index = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
unseen_set = hdw.abstract_file(ufile_name, separator)
protos_set = hdw.abstract_file(pfile_name, None, 0)
klassified = nsc.nsc(protos_set, unseen_set)
ofile_name = os.path.splitext(ufile_name)[0] + '-nsc.txt'
with open(ofile_name, 'w') as ofile:
    for point in klassified:
        ofile.write('%s\n' % point)
try:
    import Gnuplot
except ImportError:
    print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
    sys.exit()
f, s = hdw.rnd_dim(nsc.dim)
g = Gnuplot.Gnuplot(debug=0)
g.title('NSC applied to {} with prototypes from {}'.format(os.path.split(ufile_name)[-1], os.path.split(pfile_name)[-1]))
if (f, s) != (0, 1):
    g.xlabel('feature space reduced to {}x{}'.format(f+1, s+1))
klassified_dict = {}
for p in klassified:
    klassified_dict.setdefault(p.klasse, []).append(p.features)
sorted_keys = sorted(klassified_dict.keys())
for kl in sorted_keys:
    g.replot(Gnuplot.Data(klassified_dict[kl], title=kl, cols=(f, s)))
gfile_name = os.path.splitext(ufile_name)[0] + '-nsc.ps'
g.hardcopy(gfile_name, color=1)