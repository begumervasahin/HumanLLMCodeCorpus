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
            return 0
        else:
            return 1
    def add_house(self, house, backup=False):
        if backup:
            query = "INSERT INTO Tbl_Posts_Backup VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        else:
            query = "INSERT INTO Tbl_Posts VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (house.house_link, house.title, house.price, house.m2, house.date,
                                    house.neighborhood, house.room, house.img))
        self.connection.commit()
    def clear_posts(self, day):
        query = "DELETE FROM Tbl_Posts WHERE Date LIKE '%" + day + "%'"
        self.cursor.execute(query)
        self.connection.commit()
if __name__ == "__main__":
    db = DatabasePost()
    house1 = House("link1", "title1", "100000", "100", "2022-05-01", "Neighborhood1", "3+1", "image1.jpg")
    house2 = House("link2", "title2", "150000", "120", "2022-05-02", "Neighborhood2", "2+1", "image2.jpg")
    db.add_house(house1)
    db.add_house(house2)
    print("House 1 exists:", db.check_if_house_exists("link1"))
    print("House 3 exists:", db.check_if_house_exists("link3"))
    db.clear_posts("2022-05-01")