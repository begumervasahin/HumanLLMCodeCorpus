def main() -> None:
    roster = (
        ('ipns address one', 'Name one'),
        ('ipns address two', 'Name two'),
        ('etc', 'etc')
    )
    for address, name in roster:
        print(f"Address: {address}, Name: {name}")
if __name__ == "__main__":
    main()