import socket
import threading
import sys
b1 = '127.0.0.1'
a1 = 50007
a2 = 2
def fonk1():
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        b2.bind((b1, a1))
        print("Server is running on port", a1)
        print("Waiting for connections...")
        return b2
    except socket.error as e:
        print(f"Failed to bind the server socket: {e}")
        sys.exit()
def fonk2(b2):
    b3 = []
    while len(b3) < a2:
        try:
            conn, b4 = b2.accept()
            print(f"Client connected: IP {b4[0]}, Port {b4[1]}")
            b3.append((conn, b4))
        except Exception as e:
            print("An error occurred while accepting connections:", e)
            break
    return b3
class class1(threading.Thread):
    def fonk3(self, b5, b6):
        super().fonk3()
        self.b5 = b5[0]
        self.b6 = b6[0]
    def fonk4(self):
        while True:
            try:
                b7 = self.b5.recv(1024)
                if not b7:
                    print("Client disconnected.")
                    break
                self.b6.send(b7)
            except ConnectionResetError:
                print("A client disconnected unexpectedly.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break
def fonk5():
    b2 = fonk1()
    b3 = fonk2(b2)
    b8 = class1(b3[0], b3[1])
    b9 = class1(b3[1], b3[0])
    b8.start()
    b9.start()
    b8.join()
    b9.join()
    print("Both b3 have disconnected. Server shutting down.")
    b2.close()
if b10 = = "__main__":
    fonk5()