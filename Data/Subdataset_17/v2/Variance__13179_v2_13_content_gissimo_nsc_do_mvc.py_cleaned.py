import os
import sys
import nsc
import hdw
from sets import Set as set, ImmutableSet as frozenset
MIN_PYTHON_VERSION = (2, 4)
if sys.version_info[:2] < MIN_PYTHON_VERSION:
    print(f"Python version {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or greater is required.")
    sys.exit()
def main():
    ifile_name, sigma, _, _, separator, klasse_index = hdw.handle_commands(sys.argv, 's:', ['separator=', 'classid='])
    universe = hdw.abstract_file(ifile_name, separator, klasse_index)
    hdw.fill_world(universe)
    prototypes = compute_prototypes(sigma)
    write_prototypes_to_file(ifile_name, sigma, prototypes)
    plot_with_gnuplot(ifile_name, sigma, prototypes)
def compute_prototypes(sigma):
    prototypes = {}
    for kl in nsc.welt.keys():
        nsc.computeRLs(kl)
        for pr in nsc.mvc(kl, sigma):
            if kl not in prototypes:
                prototypes[kl] = set()
            if not pr.isVoid():
                prototypes[kl].add(pr.mean)
    return prototypes
def write_prototypes_to_file(ifile_name, sigma, prototypes):
    ofile_name = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.txt"
    with open(ofile_name, 'w') as ofile:
        for kl, points in prototypes.items():
            for point in points:
                ofile.write(f"{point}\n")
def plot_with_gnuplot(ifile_name, sigma, prototypes):
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
    plot_data(g, prototypes, f, s, is_prototype=True)
    plot_data(g, nsc.welt, f, s, is_prototype=False)
    gfile_name = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.ps"
    g.hardcopy(gfile_name, color=1)
def plot_data(g, data, f, s, is_prototype):
    for kl in sorted(data.keys()):
        if len(data[kl]) == 0:
            continue
        points = [item.features for item in data[kl]]
        data[kl] = points
        title = f'** {kl} **' if is_prototype else kl
        g.replot(Gnuplot.Data(data[kl], title=title, cols=(f, s)))
if __name__ == "__main__":
    main()