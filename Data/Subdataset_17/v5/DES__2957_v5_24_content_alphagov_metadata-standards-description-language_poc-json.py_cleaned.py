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
        print(f"    \"{cell.name}\":\t{render_value(cell)},")
    print("  },")
    return True
def process_spreadsheet(metadata, spreadsheet_path):
    print(f"Validating spreadsheet {spreadsheet_path} against metadata...")
    with open(spreadsheet_path) as spreadsheet:
        instance = metadata.validate(spreadsheet)
        print("Extracting typed data from spreadsheet...")
        print("[")
        instance.extract(render_json)
        print("]")
def process_spreadsheets(metadata, spreadsheets):
    for sheet in spreadsheets:
        process_spreadsheet(metadata, sheet)
def main():
    print(f"Reading metadata from {METADATA_FILE}...")
    with open(METADATA_FILE) as metadata_file:
        metadata = slang.slang(metadata_file)
        metadata.parse()
        process_spreadsheets(metadata, SPREADSHEETS)
if __name__ == "__main__":
    main()