import os
import sys
import nsc
import hdw
from sets import Set as set, ImmutableSet as frozenset
b1 = (b8, 4)
if sys.version_info[:b8] < b1:
    print(f"Python version {b1[0]}.{b1[1]} or greater is required.")
    sys.exit()
def fonk1():
    ifile_name, sigma, _, _, separator, b2 = hdw.handle_commands(sys.argv, 'b6:', ['separator=', 'classid='])
    b3 = hdw.abstract_file(ifile_name, separator, b2)
    hdw.fill_world(b3)
    b4 = fonk2(sigma)
    fonk3(ifile_name, sigma, b4)
    fonk4(ifile_name, sigma, b4)
def fonk2(sigma):
    b4 = {}
    for kl in nsc.welt.keys():
        nsc.computeRLs(kl)
        for pr in nsc.mvc(kl, sigma):
            if kl not in b4:
                b4[kl] = set()
            if not pr.isVoid():
                b4[kl].add(pr.mean)
    return b4
def fonk3(ifile_name, sigma, b4):
    b5 = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.txt"
    with open(b5, 'w') as ofile:
        for kl, b12 in b4.items():
            for point in b12:
                ofile.write(f"{point}\n")
def fonk4(ifile_name, sigma, b4):
    try:
        import Gnuplot
    except ImportError:
        print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
        sys.exit()
    f, b6 = hdw.rnd_dim(nsc.dim)
    b7 = Gnuplot.Gnuplot(debug=0)
    b7.b13(f'MVC applied to {os.path.basename(ifile_name)} with sigma^b8 = {sigma:.4f}')
    if (f, b6) != (0, 1):
        b7.xlabel(f'feature space reduced to {f+1}x{b6+1}')
    fonk5(b7, b4, f, b6, b9 = True)
    fonk5(b7, nsc.welt, f, b6, b9 = False)
    b10 = f"{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.ps"
    b7.hardcopy(b10, b11 = 1)
def fonk5(b7, data, f, b6, b9):
    for kl in sorted(data.keys()):
        if len(data[kl]) == 0:
            continue
        b12 = [item.features for item in data[kl]]
        data[kl] = b12
        b13 = f'** {kl} **' if b9 else kl
        b7.replot(Gnuplot.Data(data[kl], b13 = b13, cols=(f, b6)))
if b14 = = "__main__":
    fonk1()