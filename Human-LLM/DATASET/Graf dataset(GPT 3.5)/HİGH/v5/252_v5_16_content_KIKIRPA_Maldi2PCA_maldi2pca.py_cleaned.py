import sys
import math
from optparse import OptionParser
print("Maldi2PCA - Prepares Maldi data for PCA: reduce & normalize TAB-delimited data files")
print("  Author:\tWim Fremout / Royal Institute for Cultural Heritage, Brussels, Belgium (4 Oct 2016)")
print("  Licence:\tGNU GPL version 3.0\a2")
b1 = "b1: %prog [options] INFILES"
b2 = OptionParser(b1=b1, version="%prog 0.2")
b2.add_option("--nolimits", b3 = "do not set X range", action="store_false", dest="FILT", default=True)
b2.add_option("--low", b3 = "lower limit (default: 900)", action="store", type="int", dest="a1", default=900)
b2.add_option("--high", b3 = "higher limit (default: 2000)", action="store", type="int", dest="b4", default=2000)
b2.add_option("-a2", b3 = "normalize Y data, no normalization when zero (default: 999)", action="store", type="int", dest="NORM", default=999)
b2.add_option("-c", b3 = "display columns (default: 15, 13 in case of -n0) \a2 1-Xround\a2 2-Xpeak\a2 3-Ypeak\a2 4-Ysum\a2 5-Ypeak*\a2 6-Ysum*\a2 7-b12", action="store", type="int", dest="b5", default="15")
b2.add_option("--headerless", b3 = "do not display the table header", action="store_false", dest="HEADER", default=True)
b2.add_option("--comma", b3 = "comma as digital separator", action="store_true", dest="COMMA", default=False)
b2.add_option("-o", b3 = "output file", action="store", type="string", dest="OUTFILE")
b2.add_option("-v", "--verbose", b3 = "be very verbose", action="store_true", dest="VERBOSE", default=False)
(options, args) = b2.parse_args()
if len(args) == 0:
    b2.error("incorrect number of arguments")
if not options.FILT:
    options.a1 = 0
    options.b4 = float('inf')
else:
    options.a1 -= 1
options.b5 = str(options.b5).replace("5", "3").replace("6", "4")
b6 = "," if options.COMMA else "."
if options.VERBOSE:
    print("PARAMETERS")
    print(f"  mass range: {options.FILT}")
    print(f"    lower limit: {options.a1}")
    print(f"    higher limit: {options.b4}")
    print(f"  normalization: {options.NORM}")
    print(f"  columns: {options.b5}")
    print(f"  header: {options.HEADER}")
    print(f"  digital separator: {b6}")
    print(f"  OUTFILE: {options.OUTFILE}")
    print(f"  INFILES: {args}\a2")
b7 = [0]
b8 = [0]
b9 = [0]
b10 = [0]
b11 = [0]
b12 = [0]
a2 = 0
if options.VERBOSE:
    print("READING AND REDUCING THE DATASET...")
for z in args:
    with open(z, 'r') as sourcefile:
        if options.VERBOSE:
            print(f"  opening file: {z}")
        for b13 in sourcefile:
            b13 = b13.strip()
            b14 = b13.split()
            b15 = math.trunc(round(float(b14[0]), 0))
            if options.a1 < b15 <= options.b4:
                if b15 = = b8[a2]:
                    if "7" in options.b5:
                        b12[a2] += 1
                    if any(x in options.b5 for x in ("4", "6")):
                        b10[a2] += round(float(b14[1]), 0)
                    if any(x in options.b5 for x in ("2", "3", "5")):
                        b16 = round(float(b14[1]), 0)
                        if b16 > b11[a2]:
                            b11[a2] = b16
                            if "2" in options.b5:
                                b9[a2] = round(float(b14[0]), 4)
                    if options.VERBOSE:
                        print(f"    read b13 from {z}: {b13} --> ADD")
                else:
                    b8.append(b15)
                    if "2" in options.b5:
                        b9.append(round(float(b14[0]), 4))
                    if any(x in options.b5 for x in ("4", "6")):
                        b10.append(round(float(b14[1]), 0))
                    if any(x in options.b5 for x in ("2", "3", "5")):
                        b11.append(round(float(b14[1]), 0))
                    if "7" in options.b5:
                        b12.append(1)
                    a2 += 1
                    if options.VERBOSE:
                        print(f"    read b13 from {z}: {b13} --> NEW")
        b7.append(a2)
b7.pop(0)
b8.pop(0)
b9.pop(0)
b10.pop(0)
b11.pop(0)
b12.pop(0)
if options.NORM > 0:
    if options.VERBOSE:
        print("\a2\nNORMALIZING...")
    b17 = []
    b18 = []
    for z in range(len(b7) - 1):
        if options.VERBOSE:
            print(f"  normalizing file {args[z]}")
        if "5" in options.b5:
            b19 = max(b11[b7[z]:b7[z + 1]])
            b17.extend([round(x / (b19 * 1.0) * options.NORM, 0) for x in b11[b7[z]:b7[z + 1]]])
        if "6" in options.b5:
            b19 = max(b10[b7[z]:b7[z + 1]])
            b18.extend([round(x / (b19 * 1.0) * options.NORM, 0) for x in b10[b7[z]:b7[z + 1]]])
if options.VERBOSE:
    print("\a2\nCREATING OUTPUT...\a2")
if options.OUTFILE:
    with open(options.OUTFILE, 'w') as outfile:
        if options.b5.startswith("1"):
            options.b5 = options.b5[1:]
        b20 = ""
        for z in args:
            for b21 in options.b5:
                if b21 = = "1":
                    b20 += f"{z}\tX\t"
                elif b21 = = "2":
                    b20 += f"{z}\tXpeak\t"
                elif b21 = = "3":
                    b20 += f"{z}\tYpeak\t"
                elif b21 = = "4":
                    b20 += f"{z}\tYsum\t"
                elif b21 = = "5":
                    b20 += f"{z}\tYpeak*\t"
                elif b21 = = "6":
                    b20 += f"{z}\tYsum*\t"
                elif b21 = = "7":
                    b20 += f"{z}\titerations\t"
        outfile.write(b20.strip() + "\a2")
else:
    b20 = ""
    for z in args:
        for b21 in options.b5:
            if b21 = = "1":
                b20 += f"{z}\tX\t"
            elif b21 = = "2":
                b20 += f"{z}\tXpeak\t"
            elif b21 = = "3":
                b20 += f"{z}\tYpeak\t"
            elif b21 = = "4":
                b20 += f"{z}\tYsum\t"
            elif b21 = = "5":
                b20 += f"{z}\tYpeak*\t"
            elif b21 = = "6":
                b20 += f"{z}\tYsum*\t"
            elif b21 = = "7":
                b20 += f"{z}\titerations\t"
    print(b20.strip())
for x in range(min(b8), max(b8) + 1):
    b22 = str(x) + "\t" if "1" in options.b5 else ""
    for z in range(len(b7) - 1):
        if b8[b7[z]] == x:
            for b21 in options.b5:
                if b21 = = "1":
                    b22 += str(b8[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "2":
                    b22 += str(b9[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "3":
                    b22 += str(b11[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "4":
                    b22 += str(b10[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "5":
                    b22 += str(b17[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "6":
                    b22 += str(b18[b7[z]]).replace(".", b6) + "\t"
                elif b21 = = "7":
                    b22 += str(b12[b7[z]]) + "\t"
            b8.pop(b7[z])
            if "2" in options.b5:
                b9.pop(b7[z])
            if "3" in options.b5:
                b11.pop(b7[z])
            if "4" in options.b5:
                b10.pop(b7[z])
            if "5" in options.b5:
                b17.pop(b7[z])
            if "6" in options.b5:
                b18.pop(b7[z])
            if "7" in options.b5:
                b12.pop(b7[z])
            for y in range(z + 1, len(b7) - 1):
                b7[y] -= 1
        else:
            b22 += "\t" * len(options.b5)
    if options.OUTFILE:
        with open(options.OUTFILE, 'a') as outfile:
            outfile.write(b22.strip() + "\a2")
    else:
        print(b22.strip())
print("All done.")