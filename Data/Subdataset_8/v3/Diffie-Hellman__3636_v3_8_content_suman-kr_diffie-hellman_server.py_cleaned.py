import socket
def print_header(title):
    print("\n" + "*" * 27)
    print(f"* {title.center(23)} *")
    print("*" * 27)
def get_prime_and_base():
    prime = int(input("Enter the prime number: "))
    base = int(input("Enter the base number: "))
    return prime, base
def get_secrets():
    alice_secret = int(input("Enter Alice's secret number: "))
    bob_secret = int(input("Enter Bob's secret number: "))
    return alice_secret, bob_secret
def diffie_hellman_key_exchange(prime, base, alice_secret, bob_secret):
    print_header("Diffie-Hellman Key Exchange")
    print("\nPublicly Shared Variables:")
    print(f"  Prime Number: {prime}")
    print(f"  Base Number:  {base}")
    a_public = (base ** alice_secret) % prime
    b_public = (base ** bob_secret) % prime
    print("\nAlice Sends Over Public Channel:", a_public)
    print("Bob Sends Over Public Channel:", b_public)
    alice_shared_secret = (b_public ** alice_secret) % prime
    bob_shared_secret = (a_public ** bob_secret) % prime
    if alice_shared_secret == bob_shared_secret:
        print("\nShared Secrets Match!")
        print("Connection Established")
    return alice_shared_secret, bob_shared_secret
def establish_server(alice_secret, bob_secret, shared_secret):
    print("\nSetting up server for shared secret exchange...")
    server_socket = socket.socket()
    host = socket.gethostname()
    port = 51125
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Waiting for incoming connections...")
    while True:
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)
        client_socket.send(str(shared_secret).encode())
        client_socket.close()
if __name__ == "__main__":
    prime_number, base_number = get_prime_and_base()
    alice_secret_number, bob_secret_number = get_secrets()
    alice_shared_secret, bob_shared_secret = diffie_hellman_key_exchange(
        prime_number, base_number, alice_secret_number, bob_secret_number
    )
    establish_server(alice_secret_number, bob_secret_number, alice_shared_secret)