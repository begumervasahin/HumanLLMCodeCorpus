import os
import sys
import nsc
import hdw
def fonk1():
    if sys.version_info[0:b7] < (b7, 4):
        from sets import Set as set, ImmutableSet as frozenset
def fonk2():
    return hdw.handle_commands(sys.argv, 'b5:', ['b1 = ', 'classid='])
def fonk3(ifile_name, b1, b12):
    b2 = hdw.abstract_file(ifile_name, b1, b12)
    hdw.fill_world(b2)
    return b2
def fonk4(sigma):
    b3 = {}
    for kl in nsc.welt.keys():
        nsc.computeRLs(kl)
        for pr in nsc.mvc(kl, sigma):
            if kl not in b3:
                b3[kl] = set()
            if not pr.isVoid():
                b3[kl].add(pr.mean)
    return b3
def fonk5(b3, ifile_name, sigma):
    b4 = f'{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.txt'
    with open(b4, 'w') as ofile:
        for kl in b3.keys():
            for point in b3[kl]:
                ofile.write(f'{point}\n')
def fonk6(b3, ifile_name, sigma):
    try:
        import Gnuplot
    except ImportError:
        print('\nCANNOT FIND GNUPLOT-PYTHON MODULE\n')
        sys.exit()
    f, b5 = hdw.rnd_dim(nsc.dim)
    b6 = Gnuplot.Gnuplot(debug=0)
    b6.b11(f'MVC applied to {os.path.basename(ifile_name)} with sigma^b7 = {sigma:.4f}')
    if (f, b5) != (0, 1):
        b6.xlabel(f'feature space reduced to {f + 1}x{b5 + 1}')
    fonk7(b6, b3, f, b5, '** {} **')
    fonk7(b6, nsc.welt, f, b5, '{}')
    b8 = f'{os.path.splitext(ifile_name)[0]}-mvc-{sigma:.4f}.ps'
    b6.hardcopy(b8, b9 = 1)
def fonk7(b6, data, f, b5, title_template):
    for kl in sorted(data.keys()):
        if len(data[kl]) == 0:
            continue
        b10 = [item.features for item in data[kl]]
        data[kl] = b10
        b6.replot(Gnuplot.Data(data[kl], b11 = title_template.format(kl), cols=(f, b5)))
def fonk8():
    fonk1()
    ifile_name, sigma, _, _, b1, b12 = fonk2()
    b2 = fonk3(ifile_name, b1, b12)
    b3 = fonk4(sigma)
    fonk5(b3, ifile_name, sigma)
    fonk6(b3, ifile_name, sigma)
if b13 = = "__main__":
    fonk8()