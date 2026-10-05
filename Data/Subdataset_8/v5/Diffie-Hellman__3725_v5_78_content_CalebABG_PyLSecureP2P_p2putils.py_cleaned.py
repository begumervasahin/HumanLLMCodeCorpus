import ctypes
import struct
import sys
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
packet_ack_format = "i"
packet_header_format = f"3I{packet_ack_format}I"
packet_header_size = struct.calcsize(packet_header_format)
packet_transfer_timeout = 4
cipher_block_size = 32
use_mtu_read_size = False
transfer_timeout = 6
udp_mtu_size = 128 if use_mtu_read_size else 2 ** 12
receive_buffer = udp_mtu_size
file_read_size = udp_mtu_size
def checksum2(data):
    return ctypes.c_ushort(zlib.crc32(data) % (2 ** 32)).value
def aes_read_file(session_key, file_path, source_port, destination_port):
    file_packets = []
    block_size = cipher_block_size
    iv = get_random_bytes(16)
    try:
        with open(file_path, 'rb') as input_file:
            seq_num = 0
            while True:
                if use_mtu_read_size:
                    file_bytes_read = input_file.read(udp_mtu_size - block_size - 24)
                else:
                    file_bytes_read = input_file.read(file_read_size)
                if not file_bytes_read:
                    break
                encryption_suite = AES.new(session_key, AES.MODE_CBC, iv)
                cipher_text = encryption_suite.encrypt(pad(file_bytes_read, block_size))
                cipher_text_len = len(cipher_text)
                iv_len = len(iv)
                str_format = f"LL{cipher_text_len}s{iv_len}s"
                str_pack = struct.pack(str_format, cipher_text_len, iv_len, cipher_text, iv)
                packet = create_packet(source_port, destination_port, seq_num, str_pack)
                file_packets.append(packet)
                seq_num += 1
    except Exception as e:
        print(f"Failed to open file: {file_path}; err: {e}")
        sys.exit(-1)
    return file_packets
def create_packet(source_port, destination_port, sequence_num, data):
    data_size = len(data)
    data_format = f"{data_size}s"
    packet_struct_format = f"{packet_header_format}{data_format}"
    packet_size_bytes = struct.calcsize(packet_struct_format)
    packet_data_bytes = data
    packet_data_struct = struct.pack(data_format, packet_data_bytes)
    packet_chksum = checksum2(packet_data_struct)
    packet_struct = struct.pack(
        packet_struct_format,
        source_port,
        destination_port,
        packet_chksum,
        sequence_num,
        packet_size_bytes,
        packet_data_bytes
    )
    return packet_struct
def unpack_packet(packet):
    unpack_header = struct.unpack(packet_header_format, packet[:packet_header_size])
    unpack_packet_size = unpack_header[-1]
    unpack_data_size = unpack_packet_size - packet_header_size
    unpack_packet = struct.unpack(f"{packet_header_format}{unpack_data_size}s", packet)
    return unpack_packet
def pack_ack(packet):
    return struct.pack(packet_ack_format, packet[-3])
def unpack_ack(ack_bytes):
    return struct.unpack(packet_ack_format, ack_bytes)[0]