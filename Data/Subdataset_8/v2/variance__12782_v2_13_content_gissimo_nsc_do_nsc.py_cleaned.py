import os
import sys
import nsc_algorithm as nsc
import file_handling_wrapper as hdw
if sys.version_info[0:2] < (2, 4):
    from sets import Set as set, ImmutableSet as frozenset
unseen_file, _, prototype_file, _, separator, class_index = hdw.handle_commands(sys.argv, 'p:', ['separator=', 'classid='])
unseen_data = hdw.abstract_file(unseen_file, separator)
prototype_data = hdw.abstract_file(prototype_file, None, 0)
classified_points = nsc.nsc(prototype_data, unseen_data)
output_file = '%s-nsc.txt' % (os.path.splitext(unseen_file)[0])
with open(output_file, 'w') as output:
    for point in classified_points:
        output.write('%s\n' % (point))
try:
    import Gnuplot
except ImportError:
    print('\nGnuplot module not found.\n')
    sys.exit()
reduced_dimensions = hdw.random_dimensions(nsc.dimension)
plot = Gnuplot.Gnuplot(debug=0)
plot.title('NSC applied to %r with prototypes from %r' % (unseen_file.split(os.sep)[-1], prototype_file.split(os.sep)[-1]))
if reduced_dimensions != (0, 1):
    plot.xlabel('Feature space reduced to %dx%d' % (reduced_dimensions[0] + 1, reduced_dimensions[1] + 1))
classified_dict = {}
for point in classified_points:
    if point.class_label not in classified_dict:
        classified_dict[point.class_label] = []
    classified_dict[point.class_label].append(point.features)
sorted_classes = sorted(classified_dict.keys())
for class_label in sorted_classes:
    plot.replot(Gnuplot.Data(classified_dict[class_label], title=class_label, cols=reduced_dimensions))
plot_file = '%s-nsc.ps' % (os.path.splitext(unseen_file)[0])
plot.hardcopy(plot_file, color=1)