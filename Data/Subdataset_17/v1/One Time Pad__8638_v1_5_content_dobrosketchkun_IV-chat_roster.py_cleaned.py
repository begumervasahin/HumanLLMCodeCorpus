def main():
    roster = (
        ('ipns adrres one', 'Name one'),
        ('ipns adrres two', 'Name two'),
        ('etc', 'etc')
    )
    for address, name in roster:
        print(f"Address: {address}, Name: {name}")
if __name__ == "__main__":
    main()