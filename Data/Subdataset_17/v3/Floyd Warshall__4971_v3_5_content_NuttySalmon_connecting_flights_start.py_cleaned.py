from shortest import Database, ConnectingFlights, console
def main():
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = 27017
    DATABASE_NAME = "connecting_flight"
    db = Database(DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)
    connecting_flights = ConnectingFlights(db)
    console.menu(db, connecting_flights)
    console.clear()
if __name__ == '__main__':
    main()