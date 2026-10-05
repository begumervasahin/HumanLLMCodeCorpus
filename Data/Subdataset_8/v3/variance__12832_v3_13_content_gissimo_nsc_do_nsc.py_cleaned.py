import os
import sys
import nsc_algorithm as nsc
import file_handling_wrapper as hdw
if sys.version_info < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
unseen_file, _, prototype_file, _, separator, class_index = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
unseen_data = hdw.abstract_file(unseen_file, separator)
prototype_data = hdw.abstract_file(prototype_file, None, 0)
classified_points = nsc.nsc(prototype_data, unseen_data)
output_file = f"{os.path.splitext(unseen_file)[0]}-nsc.txt"
with open(output_file, 'w') as output:
    for point in classified_points:
        output.write(f"{point}\n")
try:
    import Gnuplot
except ImportError:
    print('\nGnuplot module not found.\n')
    sys.exit()
reduced_dimensions = hdw.random_dimensions(nsc.dimension)
plot = Gnuplot.Gnuplot(debug=0)
plot.title(f"NSC applied to '{os.path.basename(unseen_file)}' with prototypes from '{os.path.basename(prototype_file)}'")
if reduced_dimensions != (0, 1):
    plot.xlabel(f"Feature space reduced to {reduced_dimensions[0] + 1}x{reduced_dimensions[1] + 1}")
classified_dict = {}
for point in classified_points:
    classified_dict.setdefault(point.class_label, []).append(point.features)
sorted_classes = sorted(classified_dict.keys())
for class_label in sorted_classes:
    plot.replot(Gnuplot.Data(classified_dict[class_label], title=class_label, cols=reduced_dimensions))
plot_file = f"{os.path.splitext(unseen_file)[0]}-nsc.ps"
plot.hardcopy(plot_file, color=1)