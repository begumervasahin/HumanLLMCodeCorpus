import slang
METADATA = "poc.slang"
SPREADSHEETS = ["office-supplies-order.ods", "office-supplies-order.ods"]
def render_value(cell):
    if isinstance(cell.type, slang.slang_String):
        return f"\"{cell.value()}\""
    else:
        return cell.value()
def render_json(result, row):
    print("  {")
    for c in row:
        print(f"    \"{c.name}\":\t{render_value(c)},")
    print("  },")
    return True
def process_spreadsheets(metadata, spreadsheets):
    for sheet in spreadsheets:
        print(f"Validating spreadsheet {sheet} against metadata...")
        instance = metadata.validate(open(sheet))
        print("Extracting typed data from spreadsheet...")
        print("[")
        instance.extract(render_json)
        print("]")
if __name__ == "__main__":
    print(f"Reading metadata from {METADATA}...")
    metadata = slang.slang(open(METADATA))
    metadata.parse()
    process_spreadsheets(metadata, SPREADSHEETS)