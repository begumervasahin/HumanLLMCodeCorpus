class District:
    def __init__(self, district_leader, companionships=None):
        self.district_leader = district_leader
        self.companionships = companionships or []
    def add_companionship(self, companionship):
        self.companionships.append(companionship)
    def __str__(self):
        district_info = f'District Leader: {self.district_leader}\n'
        companions_info = ''.join(str(comp) for comp in self.companionships)
        return district_info + companions_info
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f'{self.first_name} {self.last_name}\n'
class Hometeacher(Person):
    def get_name(self):
        return f'{self.first_name} {self.last_name}'
class Hometeachee(Person):
    pass
class Companionship:
    def __init__(self, companions=None, hometeachees=None):
        self.companions = companions or []
        self.hometeachees = hometeachees or []
    def __str__(self):
        companions_info = ''.join(str(comp) for comp in self.companions)
        hometeachees_info = ''.join(str(teachee) for teachee in self.hometeachees)
        return companions_info + hometeachees_info
if __name__ == "__main__":
    leader = Hometeacher("John", "Doe")
    hometeachee1 = Hometeachee("Alice", "Smith")
    hometeachee2 = Hometeachee("Bob", "Johnson")
    companionship = Companionship([leader], [hometeachee1, hometeachee2])
    district = District("District Leader", [companionship])
    print(district)