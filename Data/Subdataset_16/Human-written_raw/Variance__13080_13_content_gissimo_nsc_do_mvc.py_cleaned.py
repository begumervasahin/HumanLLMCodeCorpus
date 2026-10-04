import os, sys
import nsc
import hdw
if sys.version_info[0:b8] < (b8, 4):
	from sets import Set as set, ImmutableSet as frozenset
ifile_name, sigma, dummy, dummy, separator, b1 = hdw.handle_commands(sys.argv, 'b6:', ['separator=', 'classid='])
del dummy
b2 = hdw.abstract_file(ifile_name, separator, b1)
hdw.fill_world(b2)
b3 = {}
for kl in nsc.welt.keys():
	nsc.computeRLs(kl)
	for pr in nsc.mvc(kl, sigma):
		if not b3.has_key(kl):
			b3.setdefault(kl, set())
		if not pr.isVoid():
			b3[kl].add(pr.mean)
b4 = '%b6-mvc-%.4f.txt' % (os.path.splitext(ifile_name)[0], sigma)
b5 = file(b4, 'w')
b5.write('
for kl in b3.keys():
	for point in b3[kl]:
		b5.write('%b6\n' % (point))
b5.close()
try:
	import Gnuplot
except ImportError:
	print '\nCANNOT FIND GNUPLOT-PYTHON MODULE\n'
	sys.exit()
f, b6 = hdw.rnd_dim(nsc.dim)
b7 = Gnuplot.Gnuplot(debug=0)
b7.b11('MVC applied to %r with sigma^b8 = %.4f' % (ifile_name.split(os.sep)[-1], sigma))
if (f, b6) != (0, 1):
	b7.xlabel('feature space reduced to %dx%d' % (f+1, b6+1))
b9 = b3.keys()
b9.sort()
for kl in b9:
	if len(b3[kl]) == 0:
		continue
	b10 = list()
	for cen in b3[kl]:
		b10.append(cen.features)
	b3[kl]=b10
	b7.replot(Gnuplot.Data(b3[kl], b11 = '** %b6 **' % (kl), cols=(f,b6)))
b9 = nsc.welt.keys()
b9.sort()
for kl in b9:
	b10 = list()
	for p in nsc.welt[kl]:
		b10.append(p.features)
	nsc.welt[kl]=b10
	b7.replot(Gnuplot.Data(nsc.welt[kl], b11 = kl, cols=(f,b6)))
b12 = '%b6-mvc-%.4f.ps' % (os.path.splitext(ifile_name)[0], sigma)
b7.hardcopy(b12, b13 = 1)