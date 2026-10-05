import sys
import math
from optparse import OptionParser
def fonk1():
    print("Maldi2PCA - Prepares Maldi data for PCA: reduce & normalize TAB-delimited data files")
    print("  Author:\tWim Fremout / Royal Institute for Cultural Heritage, Brussels, Belgium (4 Oct 2016)")
    print("  Licence:\tGNU GPL version 3.0\n")
def fonk2():
    b1 = "b1: %prog [options] INFILES"
    b2 = OptionParser(b1=b1, version="%prog 0.2")
    b2.add_option("--nolimits", b3 = "do not set X range", action="store_false", dest="FILT", default=True)
    b2.add_option("--low", b3 = "lower limit (default: 900)", action="store", type="int", dest="LOW", default=900)
    b2.add_option("--high", b3 = "higher limit (default: 2000)", action="store", type="int", dest="HIGH", default=2000)
    b2.add_option("-n", b3 = "normalize Y data, no normalization when zero (default: 999)", action="store", type="int", dest="b23", default=999)
    b2.add_option("-c", b3 = "display columns (default: 15, 13 in case of -n0) \n 1-Xround\n 2-Xpeak\n 3-Ypeak\n 4-Ysum\n 5-Ypeak*\n 6-Ysum*\n 7-b8", action="store", type="int", dest="b17", default="15")
    b2.add_option("--headerless", b3 = "do not display the table header", action="store_false", dest="HEADER", default=True)
    b2.add_option("--comma", b3 = "comma as digital separator", action="store_true", dest="COMMA", default=False)
    b2.add_option("-o", b3 = "output file", action="store", type="string", dest="OUTFILE")
    b2.add_option("-v", "--verbose", b3 = "be very verbose", action="store_true", dest="VERBOSE", default=False)
    return b2.parse_args()
def fonk3(options, b22):
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = [0]
    for z in b22:
        with open(z, 'r') as sourcefile:
            for b10 in sourcefile:
                b10 = b10.strip()
                b11 = b10.split()
                b12 = math.trunc(round(float(b11[0]), 0))
                if b12 <= options.LOW:
                    pass
                elif b12 > options.HIGH:
                    break
                elif b12 = = b4[-1]:
                    if "7" in options.b17:
                        b8[-1] += 1
                    if any(x in options.b17 for x in ["4", "6"]):
                        b6[-1] += round(float(b11[1]), 0)
                    if any(x in options.b17 for x in ["2", "3", "5"]):
                        b13 = round(float(b11[1]), 0)
                        if b13 > b7[-1]:
                            b7[-1] = b13
                            if "2" in options.b17:
                                b5[-1] = round(float(b11[0]), 4)
                else:
                    b4.append(b12)
                    if "2" in options.b17:
                        b5.append(round(float(b11[0]), 4))
                    if any(x in options.b17 for x in ["4", "6"]):
                        b6.append(round(float(b11[1]), 0))
                    if any(x in options.b17 for x in ["2", "3", "5"]):
                        b7.append(round(float(b11[1]), 0))
                    if "7" in options.b17:
                        b8.append(1)
                    b9.append(len(b4) - 1)
    return b4, b5, b6, b7, b8, b9
def fonk4(options, b7, b6, b9):
    b14 = []
    b15 = []
    if options.b23 > 0:
        for z in range(len(b9) - 1):
            if "5" in options.b17:
                b16 = max(b7[b9[z]:b9[z + 1]])
                for x in b7[b9[z]:b9[z + 1]]:
                    b14.append(round(x / (b16 * 1.0) * options.b23, 0))
            if "6" in options.b17:
                b16 = max(b6[b9[z]:b9[z + 1]])
                for x in b6[b9[z]:b9[z + 1]]:
                    b15.append(round(x / (b16 * 1.0) * options.b23, 0))
    return b14, b15
def fonk5(options, b22, b4, b5, b7, b6, b14, b15, b8, b9):
    with open(options.OUTFILE, 'w') as outfile:
        if options.b17[0] == "1":
            options.b17 = options.b17.replace("1", "", 1)
            b18 = True
        else:
            b18 = False
        if options.HEADER:
            b19 = ""
            b20 = ""
            if b18:
                b19 += "\t"
                b20 += "X\t"
            for z in b22:
                for y in range(len(options.b17)):
                    if options.b17[y] == "1":
                        b19 += z + "\t"
                        b20 += "X\t"
                    elif options.b17[y] == "2":
                        b19 += z + "\t"
                        b20 += "Xpeak\t"
                    elif options.b17[y] == "3":
                        b19 += z + "\t"
                        b20 += "Ypeak\t"
                    elif options.b17[y] == "4":
                        b19 += z + "\t"
                        b20 += "Ysum\t"
                    elif options.b17[y] == "5":
                        b19 += z + "\t"
                        b20 += "Ypeak*\t"
                    elif options.b17[y] == "6":
                        b19 += z + "\t"
                        b20 += "Ysum*\t"
                    elif options.b17[y] == "7":
                        b19 += z + "\t"
                        b20 += "b8\t"
            outfile.write(b19 + "\n" + b20 + "\n")
        for x in range(min(b4), max(b4) + 1):
            b21 = ""
            if b18:
                b21 += str(x) + "\t"
            for z in range(len(b9) - 1):
                if b4[b9[z]] == x:
                    for y in range(len(options.b17)):
                        if options.b17[y] == "1":
                            b21 += str(b4[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "2":
                            b21 += str(b5[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "3":
                            b21 += str(b7[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "4":
                            b21 += str(b6[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "5":
                            b21 += str(b14[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "6":
                            b21 += str(b15[b9[z]]).replace(".", ",") + "\t"
                        elif options.b17[y] == "7":
                            b21 += str(b8[b9[z]]) + "\t"
                    b9.pop(z)
                    if "2" in options.b17:
                        b5.pop(b9[z])
                    if "3" in options.b17:
                        b7.pop(b9[z])
                    if "4" in options.b17:
                        b6.pop(b9[z])
                    if "5" in options.b17:
                        b14.pop(b9[z])
                    if "6" in options.b17:
                        b15.pop(b9[z])
                    if "7" in options.b17:
                        b8.pop(b9[z])
                    for y in range(z + 1, len(b9) - 1):
                        b9[y] -= 1
                else:
                    b21 += "\t" * len(options.b17)
            outfile.write(b21 + "\n")
def fonk6():
    fonk1()
    options, b22 = fonk2()
    if len(b22) == 0:
        b2.error("incorrect number of arguments")
    if options.b23 = = 0:
        options.b17 = options.b17.replace("5", "3")
        options.b17 = options.b17.replace("6", "4")
    b24 = "," if options.COMMA else "."
    if options.VERBOSE:
        print("PARAMETERS")
        print("  mass range:", options.FILT)
        print("    lower limit:", options.LOW)
        print("    higher limit:", options.HIGH)
        print("  normalization:", options.b23)
        print("  columns:", options.b17)
        print("  header:", options.HEADER)
        print("  digital separator:", b24)
        print("  OUTFILE:", options.OUTFILE)
        print("  INFILES:", b22, "\n")
    b4, b5, b6, b7, b8, b9 = fonk3(options, b22)
    b14, b15 = fonk4(options, b7, b6, b9)
    if options.VERBOSE:
        print("\n\nCREATING OUTPUT...\n")
    if options.OUTFILE is not None:
        fonk5(options, b22, b4, b5, b7, b6, b14, b15, b8, b9)
    print("All done.")
if b25 = = "__main__":
    fonk6()