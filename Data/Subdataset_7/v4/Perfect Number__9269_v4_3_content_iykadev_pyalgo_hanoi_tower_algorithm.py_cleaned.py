def fonk1(b1, source, auxiliary, destination):
    if b1 = = 1:
        print(f"Move disk from {source} to {destination}")
    else:
        fonk1(b1 - 1, source, destination, auxiliary)
        fonk1(1, source, auxiliary, destination)
        fonk1(b1 - 1, auxiliary, source, destination)
def fonk2(ndiscs):
    print(f"Solving Tower of Hanoi problem for {ndiscs} discs:")
    fonk1(ndiscs, "A", "B", "C")
fonk2(3)
