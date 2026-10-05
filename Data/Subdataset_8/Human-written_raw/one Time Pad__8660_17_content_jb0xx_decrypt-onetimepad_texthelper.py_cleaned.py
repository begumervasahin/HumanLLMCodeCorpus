def hex_to_nums( msg ):
	len_msg = int((len(msg)/2))
	bytes_array = [0] * len_msg
	for i in range(len_msg):
		digit1 = hex_num_helper(msg[2*i])
		digit2 = hex_num_helper(msg[2*i + 1])
		bytes_array[i] = 16*digit1 + digit2
	return bytes_array
def nums_to_hex( nums ):
	return [hex(n).upper()[2:] for n in nums]
def hex_num_helper( hexVal ):
	if ord(hexVal) < 65:
		val = int(hexVal)
	else:
		val = ord(hexVal.upper()) - 55
	return val
def bytes_to_chars( bytesArray ):
	char_list = []
	for b in bytesArray:
		char_list.append(chr(b))
	return char_list
def xor_chrs( chrs ):
	val = 0
	for c in chrs:
		val ^= ord(c)
	return chr(val)