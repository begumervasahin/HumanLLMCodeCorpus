from shortest import Database, ConnectingFlights, console
def main():
    db = Database('localhost', 27017, "connecting_flight")
    cf = ConnectingFlights(db)
    console.menu(db, cf)
    console.clear()
if __name__ == '__main__':
    main()