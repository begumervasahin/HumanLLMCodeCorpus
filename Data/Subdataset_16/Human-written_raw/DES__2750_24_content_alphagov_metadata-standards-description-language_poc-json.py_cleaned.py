import slang
b1 = "poc.slang"
b2 = ["office-supplies-order.ods", "office-supplies-order.ods"]
def fonk1(cell):
    if isinstance(cell.type, slang.slang_String):
        return ("\"%s\"" % cell.value())
    else:
        return cell.value()
def fonk2(result, row):
    print("  {")
    for c in row:
        print("    \"%s\":\t%s," % (c.name, fonk1(c)))
    print("  },")
    return True
print("Reading b3 from %s..." % b1)
b3 = slang.slang(open(b1))
b3.parse()
for sheet in b2:
    print("Validating spreadsheet %s against b3..." % sheet)
    b4 = b3.validate(open(sheet))
    print("Extracting typed data from spreadsheet...")
    print("[")
    b4.extract(render_json)
    print("]")