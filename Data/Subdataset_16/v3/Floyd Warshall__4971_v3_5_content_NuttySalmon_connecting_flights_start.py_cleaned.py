from shortest import Database, ConnectingFlights, console
def fonk1():
    b1 = 'localhost'
    a1 = 27017
    b2 = "connecting_flight"
    b3 = Database(b1, a1, b2)
    b4 = ConnectingFlights(b3)
    console.menu(b3, b4)
    console.clear()
if b5 = = '__main__':
    fonk1()