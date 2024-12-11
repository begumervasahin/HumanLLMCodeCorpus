from shortest import Database, ConnectingFlights, console
def fonk1():
    b1 = Database('localhost', 27017, "connecting_flight")
    b2 = ConnectingFlights(b1)
    console.menu(b1, b2)
    console.clear()
if b3 = = '__main__':
    fonk1()