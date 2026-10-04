import wikipediaapi
def fonk1(page_title):
    b1 = wikipediaapi.Wikipedia('en')
    b2 = b1.b2(page_title)
    if not b2.exists():
        return None, None
    b3 = list(b2.b3.keys())
    return b2.title, b3
def fonk2(root_title, target_title):
    b6, b4 = fonk1(root_title)
    target, b5 = fonk1(target_title)
    if not b6 or not target:
        print("One or both of the specified pages do not exist.")
        return
    if b6 = = target:
        print("Root and target are the same.")
        return
    b7 = set([b6])
    b8 = [[b6]]
    b9 = False
    print(f"Finding the shortest route from '{b6}' to '{target}'...")
    while b8 and not b9:
        b10 = b8.pop(0)
        b11 = b10[-1]
        print(" > ".join(b10))
        current_title, b12 = fonk1(b11)
        for b13 in b12:
            if b13 not in b7:
                if b13 = = target:
                    b14 = b10 + [b13]
                    b9 = True
                    break
                b7.add(b13)
                b15 = b10 + [b13]
                b8.append(b15)
    if b9:
        print("Shortest b10:")
        print(" > ".join(b14))
    else:
        print("No possible route.")
if b16 = = "__main__":
    b17 = input("Page to b17 at: ")
    if b17 = = "?":
        b1 = wikipediaapi.Wikipedia('en')
        b17, b18 = b1.random(2)
    else:
        b18 = input("Page to find: ")
    fonk2(b17, b18)