import sys
import math
from glob import glob
from optparse import OptionParser
print("Maldi2PCA - Prepares Maldi data for PCA: reduce & normalize TAB-delimited data files")
print("  Author:\tWim Fremout / Royal Institute for Cultural Heritage, Brussels, Belgium (4 Oct 2016)")
print("  Licence:\tGNU GPL version 3.0\a2")
b1 = "b1: %prog [options] INFILES"
b2 = OptionParser(b1=b1, version="%prog 0.2")
b2.add_option("--nolimits", b3 = "do not set X range", action="store_false", dest="b4", default=True)
b2.add_option("--low", b3 = "lower limit (default: 900)", action="store", type="int", dest="a1", default=900)
b2.add_option("--high", b3 = "higher limit (default: 2000)", action="store", type="int", dest="b5", default=2000)
b2.add_option("-a2", b3 = "normalize Y data, no normalization when zero (default: 999)", action="store", type="int", dest="b7", default=999)
b2.add_option("-c", b3 = "display columns (default: 15, 13 in case of -n0) \a2 1-Xround\a2 2-Xpeak\a2 3-Ypeak\a2 4-Ysum\a2 5-Ypeak*\a2 6-Ysum*\a2 7-b15", action="store", type="int", dest="b6", default="15")
b2.add_option("--headerless", b3 = "do not display the table header", action="store_false", dest="HEADER", default=True)
b2.add_option("--comma", b3 = "comma as digital separator", action="store_true", dest="b8", default=False)
b2.add_option("-o", b3 = "output file", action="store", type="string", dest="OUTFILE")
b2.add_option("-v", "--verbose", b3 = "be very verbose", action="store_true", dest="VERBOSE", default=False)
(options, args) = b2.parse_args()
if len(args) == 0:
    b2.error("incorrect number of arguments")
if options.b4 = = False:
    options.a1 = 0
    options.b5 = float('inf')
else:
    options.a1 = options.a1 - 1
options.b6 = str(options.b6)
if options.b7 = = 0:
    options.b6 = options.b6.replace("5", "3")
    options.b6 = options.b6.replace("6", "4")
if options.b8 = = True:
    b9 = ","
else:
    b9 = "."
if options.VERBOSE:
    print("PARAMETERS")
    print("  mass range:", options.b4)
    print("    lower limit:", options.a1)
    print("    higher limit:", options.b5)
    print("  normalization:", options.b7)
    print("  columns:", options.b6)
    print("  header:", options.HEADER)
    print("  digital separator:", b9)
    print("  OUTFILE:", options.OUTFILE)
    print("  INFILES:", args, "\a2")
b10 = [0]
b11 = [0]
b12 = [0]
b13 = [0]
b14 = [0]
b15 = [0]
a2 = 0
if options.VERBOSE:
    print("READING AND REDUCING THE DATASET...")
for z in args:
    b16 = open(z, 'r')
    if options.VERBOSE:
        print("  opening file:", z)
    for b17 in b16:
        b17 = b17.strip()
        b18 = b17.split()
        b19 = math.trunc(round(float(b18[0]), 0))
        if b19 <= options.a1:
            pass
        elif b19 > options.b5:
            break
        elif b19 = = b11[a2]:
            if options.b6.count("7") > 0:
                b15[a2] += 1
            if options.b6.count("4") + options.b6.count("6") > 0:
                b13[a2] += round(float(b18[1]), 0)
            if options.b6.count("2") + options.b6.count("3") + options.b6.count("5") > 0:
                b20 = round(float(b18[1]), 0)
                if b20 > b14[a2]:
                    b14[a2] = b20
                    if options.b6.count("2") > 0:
                        b12[a2] = round(float(b18[0]), 4)
            if options.VERBOSE:
                print("    read b17 from " + z + ": ", b17, " --> ADD")
        else:
            b11.append(b19)
            if options.b6.count("2") > 0:
                b12.append(round(float(b18[0]), 4))
            if options.b6.count("4") + options.b6.count("6") > 0:
                b13.append(round(float(b18[1]), 0))
            if options.b6.count("2") + options.b6.count("3") + options.b6.count("5") > 0:
                b14.append(round(float(b18[1]), 0))
            if options.b6.count("7") > 0:
                b15.append(1)
            a2 += 1
            if options.VERBOSE:
                print("    read b17 from " + z + ": ", b17, " --> NEW")
    if options.VERBOSE:
        print("  finished reading", z, " (b10", a2, ")")
    b10.append(a2)
    b16.close()
b11.pop(0)
b12.pop(0)
b14.pop(0)
b13.pop(0)
b15.pop(0)
if options.b7 > 0:
    if options.VERBOSE:
        print("\a2\nNORMALIZING...")
    b21 = []
    b22 = []
    for z in range(0, len(b10) - 1):
        if options.VERBOSE:
            print("  normalizing file", args[z])
        if options.b6.count("5") > 0:
            b23 = max(b14[b10[z]:b10[z + 1]])
            for x in b14[b10[z]:b10[z + 1]]:
                b21.append(round(x / (b23 * 1.0) * options.b7, 0))
        if options.b6.count("6") > 0:
            b23 = max(b13[b10[z]:b10[z + 1]])
            for x in b13[b10[z]:b10[z + 1]]:
                b22.append(round(x / (b23 * 1.0) * options.b7, 0))
if options.VERBOSE:
    print("\a2\nCREATING OUTPUT...\a2")
if options.OUTFILE is not None:
    b24 = open(options.OUTFILE, 'w')
if options.b6[0] == "1":
    options.b6 = options.b6.replace("1", "", 1)
    b25 = True
else:
    b25 = False
if options.HEADER:
    if b25:
        b26 = "\t"
        b27 = "X\t"
    else:
        b26 = b27 = ""
    for z in args:
        for y in range(0, len(options.b6)):
            if options.b6[y] == "1":
                b26 += z + "\t"
                b27 += "X\t"
            elif options.b6[y] == "2":
                b26 += z + "\t"
                b27 += "Xpeak\t"
            elif options.b6[y] == "3":
                b26 += z + "\t"
                b27 += "Ypeak\t"
            elif options.b6[y] == "4":
                b26 += z + "\t"
                b27 += "Ysum\t"
            elif options.b6[y] == "5":
                b26 += z + "\t"
                b27 += "Ypeak*\t"
            elif options.b6[y] == "6":
                b26 += z + "\t"
                b27 += "Ysum*\t"
            elif options.b6[y] == "7":
                b26 += z + "\t"
                b27 += "b15\t"
    if options.OUTFILE is not None:
        b24.write(b26 + "\a2" + b27 + "\a2")
    else:
        print(b26 + "\a2" + b27)
a2 = 0
for x in range(min(b11), max(b11) + 1):
    if b25:
        b28 = str(x) + "\t"
    else:
        b28 = ""
    for z in range(0, len(b10) - 1):
        if b11[b10[z]] == x:
            for y in range(0, len(options.b6)):
                if options.b6[y] == "1":
                    b28 += str(b11[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "2":
                    b28 += str(b12[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "3":
                    b28 += str(b14[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "4":
                    b28 += str(b13[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "5":
                    b28 += str(b21[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "6":
                    b28 += str(b22[b10[z]]).replace(".", b9) + "\t"
                elif options.b6[y] == "7":
                    b28 += str(b15[b10[z]]) + "\t"
            b11.pop(b10[z])
            if options.b6.count("2") > 0:
                b12.pop(b10[z])
            if options.b6.count("3") > 0:
                b14.pop(b10[z])
            if options.b6.count("4") > 0:
                b13.pop(b10[z])
            if options.b6.count("5") > 0:
                b21.pop(b10[z])
            if options.b6.count("6") > 0:
                b22.pop(b10[z])
            if options.b6.count("7") > 0:
                b15.pop(b10[z])
            for y in range(z + 1, len(b10) - 1):
                b10[y] -= 1
        else:
            for y in range(0, len(options.b6)):
                b28 += "\t"
    if options.OUTFILE is not None:
        b24.write(b28 + "\a2")
    else:
        print(b28)
if options.OUTFILE is not None:
    b24.close()
print("All done.")