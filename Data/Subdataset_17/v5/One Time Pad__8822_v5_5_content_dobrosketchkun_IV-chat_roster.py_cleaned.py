
roster = (
    ('ipns address one', 'Name one'),
    ('ipns address two', 'Name two'),
    ('etc', 'etc')
)
def print_roster(roster):
    for address, name in roster:
        print(f"IPNS Address: {address}, Name: {name}")
def main():
    print_roster(roster)
if __name__ == "__main__":
    main()