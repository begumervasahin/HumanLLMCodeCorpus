import slang
b1 = "poc.slang"
b2 = ["office-supplies-order.ods", "office-supplies-order.ods"]
def fonk1(cell):
    if isinstance(cell.type, slang.slang_String):
        return f"\"{cell.value()}\""
    return cell.value()
def fonk2(result, row):
    print("  {")
    for cell in row:
        print(f"    \"{cell.name}\": {fonk1(cell)},")
    print("  },")
    return True
def fonk3(b4, spreadsheets):
    for sheet in spreadsheets:
        print(f"Validating spreadsheet {sheet} against b4...")
        with open(sheet) as spreadsheet:
            b3 = b4.validate(spreadsheet)
            print("Extracting typed data from spreadsheet...")
            print("[")
            b3.extract(render_json)
            print("]")
def fonk4():
    print(f"Reading b4 from {b1}...")
    with open(b1) as metadata_file:
        b4 = slang.slang(metadata_file)
        b4.parse()
        fonk3(b4, b2)
if b5 = = "__main__":
    fonk4()