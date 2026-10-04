import Seed_Generator
def generate_access_key():
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives.asymmetric import dh
	parameters = dh.generate_parameters(generator=5, key_size=1024, backend=default_backend())
	a_private_key = parameters.generate_private_key()
	a_peer_public_key = a_private_key.public_key()
	b_private_key = parameters.generate_private_key()
	b_peer_public_key = b_private_key.public_key()
	a_shared_key = a_private_key.exchange(b_peer_public_key)
	b_shared_key = b_private_key.exchange(a_peer_public_key)
	if(a_shared_key == b_shared_key):
		Seed_Generator.generate_seed(a_private_key,b_private_key,a_peer_public_key,b_peer_public_key)
		return a_shared_key
	else:
		return False
generate_access_key()