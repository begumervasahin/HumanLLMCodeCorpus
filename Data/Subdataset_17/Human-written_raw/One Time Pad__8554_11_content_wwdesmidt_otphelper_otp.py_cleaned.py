alphabet = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet_chars = []
for c in alphabet:
	alphabet_chars.append(c)
message = "This is the Message!!!!! What time should we meeT? 12:30?"
key = "One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again?"
def clean(s):
	chars = []
	for c in s:
		if c.upper() in alphabet:
			chars.append(c.upper())
	return chars
def encrypt_char(m, k):
	m_int = alphabet.index(m)
	k_int = alphabet.index(k)
	c_int = (m_int + k_int) % len(alphabet)
	return alphabet_chars[c_int]
def encrypt(m, k):
	m_chars = clean(m)
	k_chars = clean(k)
	c_chars = []
	for i in range(0, len(m_chars)):
		c_chars.append(encrypt_char(m_chars[i], k_chars[i]))
	return "".join(c_chars)
def decrypt_char(m, k):
	m_int = alphabet.index(m)
	k_int = alphabet.index(k)
	c_int = (m_int - k_int) % len(alphabet)
	return alphabet_chars[c_int]
def decrypt(m, k):
	m_chars = clean(m)
	k_chars = clean(k)
	c_chars = []
	for i in range(0, len(m_chars)):
		c_chars.append(decrypt_char(m_chars[i], k_chars[i]))
	return "".join(c_chars)