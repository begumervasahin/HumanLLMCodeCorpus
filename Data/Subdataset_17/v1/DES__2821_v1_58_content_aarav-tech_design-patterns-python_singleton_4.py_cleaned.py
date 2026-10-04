
class SingletonMeta(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        print(cls.__instances)
        return cls.__instances[cls]
class DBConnector(metaclass=SingletonMeta):
    def __init__(self):
        self.status = "Not Connected"
    def disconnect(self):
        self.status = "Disconnected"
    def connect(self):
        self.status = "Connected"
def main():
    client1 = DBConnector()
    print("Client 1:", client1)
    print("Client 1 status:", client1.status)
    client2 = DBConnector()
    print("Client 2:", client2)
    client2.connect()
    print("Client 1 status after client2 connects:", client1.status)
    client1.disconnect()
    print("Client 2 status after client1 disconnects:", client2.status)
if __name__ == "__main__":
    main()