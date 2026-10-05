class District:
    def __init__(self, district_leader, companionships=None, number_of_companionships=0):
        self.district_leader = district_leader
        if companionships is None:
            self.companionships = []
        else:
            self.companionships = companionships
        self.number_of_companionships = number_of_companionships
    def add_companionship(self, companionship):
        self.companionships.append(companionship)
        self.number_of_companionships += 1
    def to_string(self):
        district_info = f'District Leader: {self.district_leader}\n'
        companions_info = ''
        for companionship in self.companionships:
            companions_info += companionship.to_string()
        return district_info + companions_info
class Hometeacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def to_string(self):
        return f'{self.first_name} {self.last_name}\n'
    def get_name(self):
        return f'{self.first_name} {self.last_name}'
class Hometeachee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.hometeaching = {}
    def to_string(self):
        return f'\t{self.first_name} {self.last_name}\n'
    def get_name(self):
        return f'{self.first_name} {self.last_name}'
class Companionship:
    def __init__(self, companions=None, hometeachees=None):
        if companions is None:
            self.companions = []
        else:
            self.companions = companions
        if hometeachees is None:
            self.hometeachees = []
        else:
            self.hometeachees = hometeachees
    def to_string(self):
        companions_info = ''
        for companion in self.companions:
            companions_info += companion.to_string()
        hometeachees_info = ''
        for hometeachee in self.hometeachees:
            hometeachees_info += hometeachee.to_string()
        return companions_info + hometeachees_info
if __name__ == "__main__":
    leader = Hometeacher("John", "Doe")
    hometeachee1 = Hometeachee("Alice", "Smith")
    hometeachee2 = Hometeachee("Bob", "Johnson")
    companionship = Companionship([leader], [hometeachee1, hometeachee2])
    district = District("District Leader", [companionship])
    print(district.to_string())