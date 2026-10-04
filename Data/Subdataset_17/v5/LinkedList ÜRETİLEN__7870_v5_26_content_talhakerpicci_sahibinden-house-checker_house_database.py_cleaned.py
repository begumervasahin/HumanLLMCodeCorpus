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
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()
    def _create_tables(self):
        query =
        self.cursor.executescript(query)
        self.connection.commit()
    def house_exists(self, link):
        query = "SELECT 1 FROM Tbl_Posts WHERE Link = ?"
        self.cursor.execute(query, (link,))
        return self.cursor.fetchone() is not None
    def add_house(self, house, backup=False):
        table_name = "Tbl_Posts_Backup" if backup else "Tbl_Posts"
        query = f
        self.cursor.execute(query, (
            house.house_link, house.title, house.price, house.m2, house.date,
            house.neighborhood, house.room, house.img
        ))
        self.connection.commit()
    def clear_posts(self, day):
        query = "DELETE FROM Tbl_Posts WHERE Date LIKE ?"
        self.cursor.execute(query, (f'%{day}%',))
        self.connection.commit()
if __name__ == "__main__":
    db_post = DatabasePost()
    house = House(
        house_link="http:
        title="Example House",
        price="100000",
        m2="100",
        date="2023-07-27",
        neighborhood="Example Neighborhood",
        room="3+1",
        img="http:
    )
    if not db_post.house_exists(house.house_link):
        db_post.add_house(house)