import slang
METADATA_FILE = "poc.slang"
SPREADSHEETS = ["office-supplies-order.ods", "office-supplies-order.ods"]
def render_value(cell):
    if isinstance(cell.type, slang.slang_String):
        return f"\"{cell.value()}\""
    return cell.value()
def render_json(result, row):
    print("  {")
    for cell in row:
        print(f"    \"{cell.name}\": {render_value(cell)},")
    print("  },")
    return True
def process_spreadsheets(metadata, spreadsheets):
    for sheet in spreadsheets:
        print(f"Validating spreadsheet {sheet} against metadata...")
        with open(sheet) as spreadsheet:
            instance = metadata.validate(spreadsheet)
            print("Extracting typed data from spreadsheet...")
            print("[")
            instance.extract(render_json)
            print("]")
def main():
    print(f"Reading metadata from {METADATA_FILE}...")
    with open(METADATA_FILE) as metadata_file:
        metadata = slang.slang(metadata_file)
        metadata.parse()
        process_spreadsheets(metadata, SPREADSHEETS)
if __name__ == "__main__":
    main()