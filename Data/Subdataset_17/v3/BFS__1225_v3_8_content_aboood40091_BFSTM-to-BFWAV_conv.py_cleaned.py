import os
import struct
import sys
import time
FWAV_HEAD = bytearray.fromhex(
    "46574156FEFF00400001010000000000000200007000000000000040000000C07001000000000100000000000000000000000000000000000000000000000000"
)
INFO_HEAD = bytearray.fromhex(
    "494E464F000000C0000000000000000000000000000000000000000000000000710000000000001471000000000000281F000000000000180300000000000028000000001F000000000000000300000000000042000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
)
def main():
    if not sys.argv[1].endswith(".bfstm"):
        print("Invalid file format. Please provide a .bfstm file.")
        print("Exiting in 5 seconds...")
        time.sleep(5)
        sys.exit(1)
    with open(sys.argv[1], "rb") as infile:
        input_bytes = infile.read()
    data_pos = struct.unpack(">I", input_bytes[0x30:0x34])[0]
    data_size = struct.unpack(">I", input_bytes[0x34:0x38])[0]
    update_fwav_and_info_headers(input_bytes, data_size)
    fstm_interleave_block_size = struct.unpack(">I", input_bytes[0x74:0x78])[0]
    fstm_interleave_smallblock_size = struct.unpack(">I", input_bytes[0x84:0x88])[0]
    fwav_interleave_block_size = calculate_fwav_interleave_block_size(
        fstm_interleave_block_size, fstm_interleave_smallblock_size
    )
    INFO_HEAD[0x48:0x4C] = (0x18 + fwav_interleave_block_size).to_bytes(4, 'big')
    INFO_HEAD[0x58:0xB2] = input_bytes[0xDC:0x136]
    data = input_bytes[data_pos:data_pos + data_size]
    fwav = FWAV_HEAD + INFO_HEAD + data
    output_filename = os.path.splitext(sys.argv[1])[0] + ".bfwav"
    with open(output_filename, "wb") as output_file:
        output_file.write(fwav)
    print(f"Conversion complete: {output_filename}")
def update_fwav_and_info_headers(input_bytes, data_size):
    FWAV_HEAD[0x0C:0x10] = (0x100 + data_size).to_bytes(4, 'big')
    FWAV_HEAD[0x28:0x2C] = data_size.to_bytes(4, 'big')
    INFO_HEAD[0x08:0x09] = input_bytes[0x60:0x61]
    INFO_HEAD[0x09:0x0A] = input_bytes[0x61:0x62]
    INFO_HEAD[0x1F:0x20] = input_bytes[0x62:0x63]
    INFO_HEAD[0x14:0x18] = input_bytes[0x6C:0x70]
    INFO_HEAD[0x0E:0x10] = struct.unpack(">H", input_bytes[0x64:0x66])[0].to_bytes(2, 'big')
    INFO_HEAD[0x10:0x14] = input_bytes[0x68:0x6C]
def calculate_fwav_interleave_block_size(fstm_interleave_block_size, fstm_interleave_smallblock_size):
    fwav_interleave_block_size = fstm_interleave_block_size - ((fstm_interleave_smallblock_size & 0xFF)
    fwav_interleave_block_size -= (((fstm_interleave_smallblock_size & 0xFF)
    fwav_interleave_block_size += fstm_interleave_smallblock_size
    return fwav_interleave_block_size
if __name__ == "__main__":
    main()