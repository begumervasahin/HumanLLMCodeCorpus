import sqlite3
class House:
    def __init__(self, house_link, title, price, m2, date, neighborhood, room, img):
        self.house_link = house_link
        self.title = title
        self.price = price
        self.m2 = m2
        self.date = date
        self.neighborhood = neighborhood
        self.room = room
        self.img = img
class DatabasePost:
    def __init__(self, db_name="Sahibinden.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect_database()
    def connect_database(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
    def create_tables(self):
        query =
        self.cursor.executescript(query)
        self.connection.commit()
    def check_if_house_exists(self, link):
        query = "SELECT 1 FROM Tbl_Posts WHERE Link = ?"
        self.cursor.execute(query, (link,))
        return self.cursor.fetchone() is not None
    def add_house(self, house, backup=False):
        table = "Tbl_Posts_Backup" if backup else "Tbl_Posts"
        query = f
        self.cursor.execute(query, (house.house_link, house.title, house.price, house.m2, house.date, house.neighborhood, house.room, house.img))
        self.connection.commit()
    def clear_posts(self, day):
        query = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.cursor.execute(query, (f"%{day}%",))
        self.connection.commit()
    def close(self):
        if self.connection:
            self.connection.close()
if __name__ == "__main__":
    db = DatabasePost()
    house = House(
        house_link="http:
        title="Beautiful House",
        price="500000",
        m2="120",
        date="2024-01-01",
        neighborhood="Downtown",
        room="3+1",
        img="http:
    )
    exists = db.check_if_house_exists(house.house_link)
    print(f"House exists: {exists}")
    if not exists:
        db.add_house(house)
        print("House added to database")
    db.clear_posts("2024-01-01")
    print("Posts cleared for the date 2024-01-01")
    db.close()