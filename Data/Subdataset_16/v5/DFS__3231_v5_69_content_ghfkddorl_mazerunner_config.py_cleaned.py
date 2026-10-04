
b1 = False
b2 = 'gray'
b3 = 'black'
b4 = 'white'
b5 = 'green'
b6 = 'orange'
def fonk1():
    return {
        "Debug Mode": b1,
        "Color Block": b2,
        "Color Block Outline": b3,
        "Color Empty": b4,
        "Color Graph": b5,
        "Color Path": b6,
    }
def fonk2(b7):
    for key, value in b7.items():
        print(f"{key}: {value}")
def fonk3():
    b7 = fonk1()
    fonk2(b7)
if b8 = = "__main__":
    fonk3()