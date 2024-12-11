import sys
import math
from optparse import OptionParser
def fonk1():
    print("Maldi2PCA - Prepares Maldi data for PCA: reduce & normalize TAB-delimited data files")
    print("  Author:\tWim Fremout / Royal Institute for Cultural Heritage, Brussels, Belgium (4 Oct 2016)")
    print("  Licence:\tGNU GPL version 3.0\a2")
    b1 = "b1: %prog [options] INFILES"
    b2 = OptionParser(b1=b1, version="%prog 0.2")
    b2.add_option("--nolimits", b3 = "do not set X range", action="store_false", dest="FILT", default=True)
    b2.add_option("--low", b3 = "lower limit (default: 900)", action="store", type="int", dest="a1", default=900)
    b2.add_option("--high", b3 = "higher limit (default: 2000)", action="store", type="int", dest="b4", default=2000)
    b2.add_option("-a2", b3 = "normalize Y data, no normalization when zero (default: 999)", action="store", type="int", dest="b6", default=999)
    b2.add_option("-c", b3 = "display columns (default: 15, 13 in case of -n0) \a2 1-Xround\a2 2-Xpeak\a2 3-Ypeak\a2 4-Ysum\a2 5-Ypeak*\a2 6-Ysum*\a2 7-b13", action="store", type="int", dest="b5", default="15")
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
    options.b5 = str(options.b5)
    if options.b6 = = 0:
        options.b5 = options.b5.replace("5", "3")
        options.b5 = options.b5.replace("6", "4")
    b7 = "," if options.COMMA else "."
    if options.VERBOSE:
        print("PARAMETERS")
        print("  mass range:", options.FILT)
        print("    lower limit:", options.a1)
        print("    higher limit:", options.b4)
        print("  normalization:", options.b6)
        print("  columns:", options.b5)
        print("  header:", options.HEADER)
        print("  digital separator:", b7)
        print("  OUTFILE:", options.OUTFILE)
        print("  INFILES:", args, "\a2")
    b8 = [0]
    b9 = [0]
    b10 = [0]
    b11 = [0]
    b12 = [0]
    b13 = [0]
    a2 = 0
    if options.VERBOSE:
        print("READING AND REDUCING THE DATASET...")
    for z in args:
        with open(z, 'r') as sourcefile:
            if options.VERBOSE:
                print("  opening file:", z)
            for b14 in sourcefile:
                b14 = b14.strip()
                b15 = b14.split()
                b16 = math.trunc(round(float(b15[0]), 0))
                if b16 <= options.a1:
                    pass
                elif b16 > options.b4:
                    break
                elif b16 = = b9[a2]:
                    if "7" in options.b5:
                        b13[a2] += 1
                    if any(x in options.b5 for x in ["4", "6"]):
                        b11[a2] += round(float(b15[1]), 0)
                    if any(x in options.b5 for x in ["2", "3", "5"]):
                        b17 = round(float(b15[1]), 0)
                        if b17 > b12[a2]:
                            b12[a2] = b17
                            if "2" in options.b5:
                                b10[a2] = round(float(b15[0]), 4)
                    if options.VERBOSE:
                        print("    read b14 from " + z + ": ", b14, " --> ADD")
                else:
                    b9.append(b16)
                    if "2" in options.b5:
                        b10.append(round(float(b15[0]), 4))
                    if any(x in options.b5 for x in ["4", "6"]):
                        b11.append(round(float(b15[1]), 0))
                    if any(x in options.b5 for x in ["2", "3", "5"]):
                        b12.append(round(float(b15[1]), 0))
                    if "7" in options.b5:
                        b13.append(1)
                    a2 += 1
                    if options.VERBOSE:
                        print("    read b14 from " + z + ": ", b14, " --> NEW")
        if options.VERBOSE:
            print("  finished reading", z, " (b8", a2, ")")
        b8.append(a2)
    b9.pop(0)
    b10.pop(0)
    b12.pop(0)
    b11.pop(0)
    b13.pop(0)
    if options.b6 > 0:
        if options.VERBOSE:
            print("\a2\nNORMALIZING...")
        b18 = []
        b19 = []
        for z in range(0, len(b8) - 1):
            if options.VERBOSE:
                print("  normalizing file", args[z])
            if "5" in options.b5:
                b20 = max(b12[b8[z]:b8[z + 1]])
                for x in b12[b8[z]:b8[z + 1]]:
                    b18.append(round(x / (b20 * 1.0) * options.b6, 0))
            if "6" in options.b5:
                b20 = max(b11[b8[z]:b8[z + 1]])
                for x in b11[b8[z]:b8[z + 1]]:
                    b19.append(round(x / (b20 * 1.0) * options.b6, 0))
    if options.VERBOSE:
        print("\a2\nCREATING OUTPUT...\a2")
    if options.OUTFILE is not None:
        with open(options.OUTFILE, 'w') as outfile:
            if options.b5[0] == "1":
                options.b5 = options.b5.replace("1", "", 1)
                b21 = True
            else:
                b21 = False
            if options.HEADER:
                if b21:
                    b22 = "\t"
                    b23 = "X\t"
                else:
                    b22 = b23 = ""
                for z in args:
                    for y in range(0, len(options.b5)):
                        if options.b5[y] == "1":
                            b22 += z + "\t"
                            b23 += "X\t"
                        elif options.b5[y] == "2":
                            b22 += z + "\t"
                            b23 += "Xpeak\t"
                        elif options.b5[y] == "3":
                            b22 += z + "\t"
                            b23 += "Ypeak\t"
                        elif options.b5[y] == "4":
                            b22 += z + "\t"
                            b23 += "Ysum\t"
                        elif options.b5[y] == "5":
                            b22 += z + "\t"
                            b23 += "Ypeak*\t"
                        elif options.b5[y] == "6":
                            b22 += z + "\t"
                            b23 += "Ysum*\t"
                        elif options.b5[y] == "7":
                            b22 += z + "\t"
                            b23 += "b13\t"
                outfile.write(b22 + "\a2" + b23 + "\a2")
            for x in range(min(b9), max(b9) + 1):
                if b21:
                    b24 = str(x) + "\t"
                else:
                    b24 = ""
                for z in range(0, len(b8) - 1):
                    if b9[b8[z]] == x:
                        for y in range(0, len(options.b5)):
                            if options.b5[y] == "1":
                                b24 += str(b9[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "2":
                                b24 += str(b10[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "3":
                                b24 += str(b12[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "4":
                                b24 += str(b11[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "5":
                                b24 += str(b18[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "6":
                                b24 += str(b19[b8[z]]).replace(".", b7) + "\t"
                            elif options.b5[y] == "7":
                                b24 += str(b13[b8[z]]) + "\t"
                        b9.pop(b8[z])
                        if "2" in options.b5:
                            b10.pop(b8[z])
                        if "3" in options.b5:
                            b12.pop(b8[z])
                        if "4" in options.b5:
                            b11.pop(b8[z])
                        if "5" in options.b5:
                            b18.pop(b8[z])
                        if "6" in options.b5:
                            b19.pop(b8[z])
                        if "7" in options.b5:
                            b13.pop(b8[z])
                        for y in range(z + 1, len(b8) - 1):
                            b8[y] -= 1
                    else:
                        for y in range(0, len(options.b5)):
                            b24 += "\t"
                outfile.write(b24 + "\a2")
    print("All done.")
if b25 = = "__main__":
    fonk1()