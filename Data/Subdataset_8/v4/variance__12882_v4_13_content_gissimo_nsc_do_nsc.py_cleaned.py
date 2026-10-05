import os
import sys
import nsc
import hdw
if sys.version_info[0:2] < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
ufile_name, _, pfile_name, _, separator, klasse_index = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
del _
unseen_set = hdw.abstract_file(ufile_name, separator)
protos_set = hdw.abstract_file(pfile_name, None, 0)
klassified = nsc.nsc(protos_set, unseen_set)
ofile_name = '%s-nsc.txt' % (os.path.splitext(ufile_name)[0])
ofile = open(ofile_name, 'w')
for point in klassified:
    ofile.write('%s\n' % (point))
ofile.close()
try:
    import Gnuplot
except ImportError:
    print '\nCANNOT FIND GNUPLOT-PYTHON MODULE\n'
    sys.exit()
f, s = hdw.rnd_dim(nsc.dim)
g = Gnuplot.Gnuplot(debug=0)
g.title('NSC applied to %r with prototypes from %r' % (ufile_name.split(os.sep)[-1], pfile_name.split(os.sep)[-1]))
if (f, s) != (0, 1):
    g.xlabel('feature space reduced to %dx%d' % (f+1, s+1))
klassified_dict = {}
for p in klassified:
    if p.klasse not in klassified_dict:
        klassified_dict[p.klasse] = []
    klassified_dict[p.klasse].append(p.features)
tmp = sorted(klassified_dict.keys())
for kl in tmp:
    g.replot(Gnuplot.Data(klassified_dict[kl], title=kl, cols=(f, s)))
gfile_name = '%s-nsc.ps' % (os.path.splitext(ufile_name)[0])
g.hardcopy(gfile_name, color=1)