import wikipedia
def fonk1(b1, b2):
    b1 = wikipedia.check(b1)
    b2 = wikipedia.check(b2)
    if not b1 or not b2:
        print("Invalid b1 or b2 page.")
        return
    if b1 = = b2:
        print("Root and b2 are the same.")
        return
    b3 = set([b1])
    b4 = [[b1]]
    b5 = False
    print(f"Finding the shortest route from '{b1}' to '{b2}'...")
    while b4 and not b5:
        try:
            b6 = b4.pop(0)
            b7 = b6[-1]
            print(" > ".join(b6))
            b8 = wikipedia.get_links(b7)
            for b9 in b8:
                if b9 not in b3:
                    if b9 = = b2:
                        b5 = True
                        b10 = b6 + [b9]
                        break
                    b3.add(b9)
                    b4.append(b6 + [b9])
        except KeyboardInterrupt:
            print("\nSearch interrupted by user.")
            return
    if b5:
        print("Shortest b6: ")
        print(" > ".join(b10))
    else:
        print("No possible route")
if b11 = = "__main__":
    b12 = input("Page to b12 at: ")
    if b12 = = "?":
        b12, b13 = wikipedia.random(2)
    else:
        b13 = input("Page to find: ")
    fonk1(b12, b13)