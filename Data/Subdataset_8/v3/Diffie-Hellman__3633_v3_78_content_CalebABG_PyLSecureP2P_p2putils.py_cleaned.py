import ctypes
import struct
import sys
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
PACKET_ACK_FORMAT = "i"
PACKET_HEADER_FORMAT = "3I{}I".format(PACKET_ACK_FORMAT)
PACKET_HEADER_SIZE = struct.calcsize(PACKET_HEADER_FORMAT)
PACKET_TRANSFER_TIMEOUT = 4
CIPHER_BLOCK_SIZE = 32
USE_MTU_READ_SIZE = False
TRANSFER_TIMEOUT = 6
UDP_MTU_SIZE = 128 if USE_MTU_READ_SIZE else 2 ** 12
RECEIVE_BUFFER = UDP_MTU_SIZE if USE_MTU_READ_SIZE else 2 ** 13
FILE_READ_SIZE = UDP_MTU_SIZE
def calculate_checksum(data):
    return (ctypes.c_ushort(int(zlib.crc32(data) % 2 ** 32))).value
def aes_read_file(session_key, file_path, source_port, destination_port):
    input_file = None
    file_packets = []
    seq_num = 0
    block_size = CIPHER_BLOCK_SIZE
    iv = get_random_bytes(16)
    try:
        input_file = open(file_path, 'rb')
        while True:
            if USE_MTU_READ_SIZE:
                file_bytes_read = input_file.read(UDP_MTU_SIZE - block_size - 24)
            else:
                file_bytes_read = input_file.read(FILE_READ_SIZE)
            if not file_bytes_read:
                break
            encryption_suite = AES.new(session_key, AES.MODE_CBC, iv)
            cipher_text = encryption_suite.encrypt(pad(file_bytes_read, block_size))
            cipher_text_len = len(cipher_text)
            iv_len = len(iv)
            str_format = "LL{}s{}s".format(cipher_text_len, iv_len)
            str_pack = struct.pack(str_format, cipher_text_len, iv_len, cipher_text, iv)
            packet = create_packet(source_port, destination_port, seq_num, str_pack)
            file_packets.append(packet)
            seq_num += 1
    except Exception as e:
        print("Failed to open file: {}; err: {}".format(file_path, e))
        sys.exit(-1)
    finally:
        if input_file is not None:
            input_file.close()
    return file_packets
def create_packet(source_port, destination_port, sequence_num, data):
    data_size = len(data)
    data_format = "{}s".format(data_size)
    packet_struct_format = PACKET_HEADER_FORMAT + data_format
    packet_size_bytes = struct.calcsize(packet_struct_format)
    packet_data_bytes = data
    packet_data_struct = struct.pack(data_format, packet_data_bytes)
    packet_chksum = calculate_checksum(packet_data_struct)
    packet_struct = struct.pack(packet_struct_format, source_port, destination_port, packet_chksum,
                                sequence_num, packet_size_bytes, packet_data_bytes)
    return packet_struct
def unpack_packet(packet):
    unpack_header = struct.unpack(PACKET_HEADER_FORMAT, packet[:PACKET_HEADER_SIZE])
    unpack_packet_size = unpack_header[-1]
    unpack_data_size = unpack_packet_size - PACKET_HEADER_SIZE
    unpack_packet = struct.unpack("{}{}s".format(PACKET_HEADER_FORMAT, unpack_data_size), packet)
    return unpack_packet
def pack_ack(packet):
    return struct.pack(PACKET_ACK_FORMAT, packet[-3])
def unpack_ack(ack_bytes):
    return struct.unpack(PACKET_ACK_FORMAT, ack_bytes)[0]
session_key = b'some_secret_key'
file_path = 'example.txt'
source_port = 1234
destination_port = 5678
file_packets = aes_read_file(session_key, file_path, source_port, destination_port)
print("Generated file packets:", file_packets)