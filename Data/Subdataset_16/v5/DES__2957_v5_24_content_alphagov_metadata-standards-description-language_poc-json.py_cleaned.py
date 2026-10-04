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
        print(f"    \"{cell.name}\":\t{fonk1(cell)},")
    print("  },")
    return True
def fonk3(b4, spreadsheet_path):
    print(f"Validating spreadsheet {spreadsheet_path} against b4...")
    with open(spreadsheet_path) as spreadsheet:
        b3 = b4.validate(spreadsheet)
        print("Extracting typed data from spreadsheet...")
        print("[")
        b3.extract(render_json)
        print("]")
def fonk4(b4, spreadsheets):
    for sheet in spreadsheets:
        fonk3(b4, sheet)
def fonk5():
    print(f"Reading b4 from {b1}...")
    with open(b1) as metadata_file:
        b4 = slang.slang(metadata_file)
        b4.parse()
        fonk4(b4, b2)
if b5 = = "__main__":
    fonk5()