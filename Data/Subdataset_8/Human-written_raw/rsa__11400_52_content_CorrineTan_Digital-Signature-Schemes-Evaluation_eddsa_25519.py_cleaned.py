import ed25519
import time
import sys
import hashlib
def ed25519test(filename):
	time1 = 0
	time2 = 0
	time3 = 0
	with open(filename) as f:
		for line in f:
			message = str.encode(line)
			digest = hashlib.sha256(message).digest()
			keygenestart = time.time()
			signing_key, verifying_key = ed25519.create_keypair()
			keygeneend = time.time()
			time1 += keygeneend - keygenestart
			signstart = time.time()
			signature = signing_key.sign(digest, encoding = "base64")
			signend = time.time()
			time2 += signend - signstart
			verifystart = time.time()
			try:
  				verifying_key.verify(signature, digest, encoding="base64")
			except ed25519.BadSignatureError:
  				print("signature is bad!")
			verifyend = time.time()
			time3 += verifyend - verifystart
	return time1, time2, time3
if __name__ == '__main__':
	time1, time2, time3 = ed25519test("".join(sys.argv[1:]))
	totaltime = time1 + time2 +time3
	print("The time used to generate key pairs:",time1)
	print("The time used to sign messages:",time2)
	print("The time used to verify messages:",time3)
	print("Total time:",totaltime)