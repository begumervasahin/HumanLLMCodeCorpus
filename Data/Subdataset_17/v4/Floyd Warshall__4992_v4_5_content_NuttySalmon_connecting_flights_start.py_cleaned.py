from shortest import Database, ConnectingFlights, console
def main():
    database_host = 'localhost'
    database_port = 27017
    database_name = "connecting_flight"
    db = Database(database_host, database_port, database_name)
    connecting_flights = ConnectingFlights(db)
    console.menu(db, connecting_flights)
    console.clear()
if __name__ == '__main__':
    main()