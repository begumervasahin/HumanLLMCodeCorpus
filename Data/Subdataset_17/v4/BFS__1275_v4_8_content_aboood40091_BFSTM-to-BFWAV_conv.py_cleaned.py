import os
import struct
import sys
import time
FWAV_HEADER = bytearray.fromhex(
    "46574156FEFF00400001010000000000000200007000000000000040000000C07001000000000100000000000000000000000000000000000000000000000000"
)
INFO_HEADER = bytearray.fromhex(
    "494E464F000000C0000000000000000000000000000000000000000000000000710000000000001471000000000000281F000000000000180300000000000028000000001F000000000000000300000000000042000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
)
def main():
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".bfstm"):
        print("Invalid input file. Please provide a .bfstm file.")
        print("\nExiting in 5 seconds...")
        time.sleep(5)
        sys.exit(1)
    input_file_path = sys.argv[1]
    with open(input_file_path, "rb") as infile:
        input_data = infile.read()
    data_pos = struct.unpack(">I", input_data[0x30:0x34])[0]
    data_size = struct.unpack(">I", input_data[0x34:0x38])[0]
    FWAV_HEADER[0x0C:0x10] = (0x100 + data_size).to_bytes(4, 'big')
    FWAV_HEADER[0x28:0x2C] = data_size.to_bytes(4, 'big')
    INFO_HEADER[0x08:0x09] = input_data[0x60:0x61]
    INFO_HEADER[0x09:0x0A] = input_data[0x61:0x62]
    INFO_HEADER[0x1F:0x20] = input_data[0x62:0x63]
    INFO_HEADER[0x14:0x18] = input_data[0x6C:0x70]
    INFO_HEADER[0x0E:0x10] = (struct.unpack(">H", input_data[0x64:0x68])[0]).to_bytes(2, 'big')
    INFO_HEADER[0x10:0x14] = input_data[0x68:0x6C]
    FSTM_interleave_block_size = struct.unpack(">I", input_data[0x74:0x78])[0]
    FSTM_interleave_small_block_size = struct.unpack(">I", input_data[0x84:0x88])[0]
    FWAV_interleave_block_size = (
        FSTM_interleave_block_size
        - ((FSTM_interleave_small_block_size & 0xFF)
        - (((FSTM_interleave_small_block_size & 0xFF)
        + FSTM_interleave_small_block_size
    )
    INFO_HEADER[0x48:0x4C] = (0x18 + FWAV_interleave_block_size).to_bytes(4, 'big')
    INFO_HEADER[0x58:0xB2] = input_data[0xDC:0x136]
    data_chunk = input_data[data_pos:data_pos + data_size]
    FWAV_file = FWAV_HEADER + INFO_HEADER + data_chunk
    output_file_path = os.path.splitext(input_file_path)[0] + ".bfwav"
    with open(output_file_path, "wb") as outfile:
        outfile.write(FWAV_file)
if __name__ == "__main__":
    main()