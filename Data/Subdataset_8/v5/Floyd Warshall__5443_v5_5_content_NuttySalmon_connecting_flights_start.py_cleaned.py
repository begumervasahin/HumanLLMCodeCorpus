from shortest import Database, ConnectingFlights, console
def main():
    database = Database('localhost', 27017, "connecting_flight")
    connecting_flights = ConnectingFlights(database)
    console.menu(database, connecting_flights)
    console.clear()
if __name__ == '__main__':
    main()