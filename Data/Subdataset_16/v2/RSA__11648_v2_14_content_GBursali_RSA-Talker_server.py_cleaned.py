import b16
import threading
from Crypto.PublicKey import RSA
class class1:
    def fonk1(self):
        self.a1 = 1423
        self.b1 = "ISO-8859-1"
        self.b2 = "UTF-8"
        self.b3 = b16.b16()
        self.b3.bind(('', self.a1))
        self.b3.listen()
        self.b4 = []
        threading.Thread(b5 = self.accept_clients).start()
    def fonk2(self):
        while True:
            conn, b6 = self.b3.accept()
            b7 = class2(conn, b6)
            self.b4.append(b7)
            print("class2 connected.")
            threading.Thread(b5 = self.handle_client, args=(b7,)).start()
    def fonk3(self, b7):
        while True:
            b8 = self.fonk6(b7.b16)
            if b8 = = '':
                continue
            b15, b9 = b8.split(':', 1)
            b10 = b9.encode(self.b1)
            try:
                b11 = RSA.importKey(b10)
                print("Public b17 received.")
                b7.fonk9(b11, b15)
            except Exception as e:
                print(f"Error importing b17: {e}")
                self.fonk4(b10, b7, b15)
    def fonk4(self, b9, b7, b12 = None):
        b13 = self.fonk5(b12)
        if b13 and b13.b17:
            try:
                b14 = b13.b17.encrypt(self.fonk7(b7.b15) + b'->' + b9, b'')[0]
                for user in self.b4:
                    if user.b15 != b7.b15:
                        user.fonk10(b14)
            except Exception as e:
                print(f"Error sending b8: {e}")
    def fonk5(self, b15):
        for b7 in self.b4:
            if b7.b15 = = b15:
                return b7
        return None
    def fonk6(self, connection):
        try:
            b8 = connection.recv(16384).decode(self.b1)
            return b8
        except Exception as e:
            print(f"Error receiving b8: {e}")
            return ''
    def fonk7(self, text):
        try:
            return text.encode(self.b2)
        except UnicodeEncodeError:
            return text.encode(self.b1)
class class2:
    def fonk8(self, connection, b18):
        self.b16 = connection
        self.b17 = None
        self.b15 = None
        self.b18 = b18
    def fonk9(self, b17, b15):
        if self.b17 is not None:
            return
        self.b17 = b17
        self.b15 = b15
    def fonk10(self, b8):
        try:
            self.b16.send(b8)
        except Exception as e:
            print(f"Error sending b8 to b7: {e}")
if b19 = = "__main__":
    b20 = class1()