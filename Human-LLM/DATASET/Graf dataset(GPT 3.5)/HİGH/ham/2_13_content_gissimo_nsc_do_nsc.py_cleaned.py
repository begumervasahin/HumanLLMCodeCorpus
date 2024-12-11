import os, sys
import nsc
import hdw
if sys.version_info[0:2] < (2, 4):
	from sets import Set as set, ImmutableSet as frozenset
ufile_name, dummy, pfile_name, dummy, separator, b1 = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
del dummy
b2 = hdw.abstract_file(ufile_name, separator)
b3 = hdw.abstract_file(pfile_name, None, 0)
b4 = nsc.nsc(b3, b2)
b5 = '%b7-nsc.txt' % (os.path.splitext(ufile_name)[0])
b6 = file(b5, 'w')
b6.write('
for point in b4:
	b6.write('%b7\n' % (point))
b6.close()
try:
	import Gnuplot
except ImportError:
	print '\nCANNOT FIND GNUPLOT-PYTHON MODULE\n'
	sys.exit()
f, b7 = hdw.rnd_dim(nsc.dim)
b8 = Gnuplot.Gnuplot(debug=0)
b8.b11('NSC applied to %r with prototypes from %r' % (ufile_name.split(os.sep)[-1], pfile_name.split(os.sep)[-1]))
if (f, b7) != (0, 1):
	b8.xlabel('feature space reduced to %dx%d' % (f+1, b7+1))
b9 = {}
for p in b4:
	if not b9.has_key(p.klasse):
		b9.setdefault(p.klasse, list())
	b9[p.klasse].append(p.features)
b10 = b9.keys()
b10.sort()
for kl in b10:
	b8.replot(Gnuplot.Data(b9[kl], b11 = kl, cols=(f,b7)))
b12 = '%b7-nsc.ps' % (os.path.splitext(ufile_name)[0])
b8.hardcopy(b12, b13 = 1)