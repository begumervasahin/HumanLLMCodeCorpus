import os
import sys
import nsc_algorithm as nsc
import file_handling_wrapper as hdw
if sys.version_info < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
unseen_file, _, prototype_file, _, separator, b1 = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
b2 = hdw.abstract_file(unseen_file, separator)
b3 = hdw.abstract_file(prototype_file, None, 0)
b4 = nsc.nsc(b3, b2)
b5 = f"{os.path.splitext(unseen_file)[0]}-nsc.txt"
with open(b5, 'w') as output:
    for point in b4:
        output.write(f"{point}\n")
try:
    import Gnuplot
except ImportError:
    print('\nGnuplot module not found.\n')
    sys.exit()
b6 = hdw.random_dimensions(nsc.dimension)
b7 = Gnuplot.Gnuplot(debug=0)
b7.b10(f"NSC applied to '{os.path.basename(unseen_file)}' with prototypes from '{os.path.basename(prototype_file)}'")
if b6 != (0, 1):
    b7.xlabel(f"Feature space reduced to {b6[0] + 1}x{b6[1] + 1}")
b8 = {}
for point in b4:
    b8.setdefault(point.class_label, []).append(point.features)
b9 = sorted(b8.keys())
for class_label in b9:
    b7.replot(Gnuplot.Data(b8[class_label], b10 = class_label, cols=b6))
b11 = f"{os.path.splitext(unseen_file)[0]}-nsc.ps"
b7.hardcopy(b11, b12 = 1)