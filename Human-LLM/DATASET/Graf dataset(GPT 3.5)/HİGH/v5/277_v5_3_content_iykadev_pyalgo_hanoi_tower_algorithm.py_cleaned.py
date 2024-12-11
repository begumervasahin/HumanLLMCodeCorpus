def fonk1(source, destination):
    print(f"Move disk from {source} to {destination}")
def fonk2(b1, source, auxiliary, destination):
    if b1 = = 1:
        fonk1(source, destination)
    else:
        fonk2(b1 - 1, source, destination, auxiliary)
        fonk1(source, destination)
        fonk2(b1 - 1, auxiliary, source, destination)
def fonk3(ndiscs):
    print(f"Solving Tower of Hanoi problem for {ndiscs} discs:")
    fonk2(ndiscs, "A", "B", "C")
fonk3(3)