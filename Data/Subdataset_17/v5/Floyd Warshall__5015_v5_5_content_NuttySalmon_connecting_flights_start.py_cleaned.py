from shortest import Database, ConnectingFlights, console
def main():
    host = 'localhost'
    port = 27017
    db_name = "connecting_flight"
    database = Database(host, port, db_name)
    connecting_flights_service = ConnectingFlights(database)
    console.menu(database, connecting_flights_service)
    console.clear()
if __name__ == '__main__':
    main()