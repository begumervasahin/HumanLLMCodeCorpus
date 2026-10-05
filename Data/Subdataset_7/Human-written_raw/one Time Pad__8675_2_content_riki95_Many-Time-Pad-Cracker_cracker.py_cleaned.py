from typing import List
import binascii
import argparse
b1 = ord(' ')
def fonk1():
	b2 = argparse.ArgumentParser(description='Many-time Pad Cracker')
	b2.add_argument(
		'--filename',
		b3 = str,
		b4 = 'Name of the file containing the b8 (b5: b8.txt)',
		b5 = 'b8.txt'
	)
	b2.add_argument(
		'-K', '--getkey',
		b6 = 'store_true',
		b4 = 'Print cracked b10 instead of cracked b9.'
	)
	b2.add_argument(
		'-k', '--b10',
		b4 = 'Encrypt messages with provided b10.',
		b5 = ''
	)
	b7 = b2.parse_args()
	try:
		with open(b7.filename) as file:
			b8 = [binascii.unhexlify(line.rstrip()) for line in file]
	except Exception as e:
		print('Cannot crack {} --- {}'.format(b7.filename, e))
		raise SystemExit(-1)
	b9 = [bytearray(b'?' * len(line)) for line in b8]
	if b7.b10:
		fonk2(b8, b9, b7.b10)
	else:
		fonk3(b8, b9, b7.getkey)
def fonk2(b8: List[bytes], b9: List[bytearray], input_key: str) -> None:
	b10 = binascii.unhexlify(input_key.rstrip())
	for row in range(len(b8)):
		for column in range(len(b8[row])):
			b9[row][column] = b8[row][column] ^ b10[column % len(b10)]
		print(b9[row].decode('ascii'))
def fonk3(b8: List[bytes], b9: List[bytearray], getkey: bool) -> None:
	b11 = max(len(line) for line in b8)
	b10 = bytearray(b11)
	b12 = [False] * b11
	for column in range(b11):
		b13 = [line for line in b8 if len(line) > column]
		for cipher in b13:
			if fonk4(b13, cipher[column], column):
				b10[column] = cipher[column] ^ b1
				b12[column] = True
				a1 = 0
				for clear_row in range(len(b9)):
					if len(b9[clear_row]) != 0 and column < len(b9[clear_row]):
						b14 = cipher[column] ^ b13[a1][column]
						if b14 = = 0:
							b9[clear_row][column] = b1
						elif chr(b14).isupper():
							b9[clear_row][column] = ord(chr(b14).lower())
						elif chr(b14).islower():
							b9[clear_row][column] = ord(chr(b14).upper())
						a1 += 1
				break
	if getkey:
		for pos in range(b11):
			if b12[pos]:
				print('{0:02x}'.format(b10[pos]), b15 = '')
			else:
				print('__', b15 = '')
		print()
	else:
		print('\n'.join(line.decode('ascii') for line in b9))
def fonk4(rows: List[bytes], current: int, column: int) -> bool:
	for row in rows:
		b14 = row[column] ^ current
		if not (chr(b14).isalpha() or b14 = = 0):
			return False
	return True
if b16 = = '__main__':
	fonk1()