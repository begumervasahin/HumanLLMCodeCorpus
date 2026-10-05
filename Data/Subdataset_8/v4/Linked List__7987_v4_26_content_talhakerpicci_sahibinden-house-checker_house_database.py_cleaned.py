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
    def __init__(self):
        self.connect_database()
    def connect_database(self):
        self.connection = sqlite3.connect("Sahibinden.db")
        self.cursor = self.connection.cursor()
        query =
        self.cursor.executescript(query)
        self.connection.commit()
    def check_if_house_exists(self, link):
        query = "SELECT * FROM Tbl_Posts WHERE Link = ?"
        self.cursor.execute(query, (link,))
        posts = self.cursor.fetchall()
        if len(posts) == 0:
            return False
        else:
            return True
    def add_house(self, house, backup=False):
        if backup:
            query = "INSERT INTO Tbl_Posts_Backup VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        else:
            query = "INSERT INTO Tbl_Posts VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (house.house_link, house.title, house.price, house.m2, house.date,
                                    house.neighborhood, house.room, house.img))
        self.connection.commit()
    def clear_posts(self, day):
        query = f"DELETE FROM Tbl_Posts WHERE Date LIKE '%{day}%'"
        self.cursor.execute(query)
        self.connection.commit()