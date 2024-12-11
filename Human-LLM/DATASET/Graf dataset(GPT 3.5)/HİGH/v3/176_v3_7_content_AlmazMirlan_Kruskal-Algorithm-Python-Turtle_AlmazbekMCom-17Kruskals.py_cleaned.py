import turtle
import time
def fonk1(text, x, y, b1 = ("Freestyle Script", 20, "normal"), b2="center", color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, b2 = b2, b1=b1)
def fonk2(start, b3, weight):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(b3)
    turtle.penup()
    turtle.goto((start[0] + b3[0]) / 2, (start[1] + b3[1]) / 2)
    turtle.write(weight, b2 = "center", b1=("Arial", 12, "normal"))
def fonk3(b5):
    for node, pos in b5.items():
        turtle.penup()
        turtle.goto(pos)
        turtle.dot(20, "green")
        fonk1(node, pos[0] + 10, pos[1] + 10, b1 = ("Arial", 16, "normal"))
def fonk4(b5, b6):
    for (start, b3), weight in b6.items():
        fonk2(b5[start], b5[b3], weight)
def fonk5(b4, y_coordinate):
    for step in b4:
        fonk1(step, 0, y_coordinate)
        y_coordinate -= 60
def fonk6(b5, b6, b7):
    turtle.pensize(15)
    turtle.fillcolor("red")
    turtle.color("red")
    for i in range(len(b7) - 1):
        start, b3 = b7[i], b7[i + 1]
        fonk2(b5[start], b5[b3], b6[(start, b3)])
    turtle.exitonclick()
def fonk7():
    turtle.title("Kruskal's Algorithm")
    turtle.bgcolor("white")
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.speed(1)
    turtle.hideturtle()
    fonk1("Kruskal's Algorithm", 0, 250, b1 = ("Freestyle Script", 50, "normal"), color="purple")
    fonk1("Almazbek Mirlan uulu Com-17", 0, -180)
    b4 = [
        "1. Sort all the b6 from low weight to high",
        "2. Take the edge with the lowest weight and add it to the spanning tree.",
        "   If adding the edge created a cycle, then reject this edge.",
        "3. Keep adding b6 until we reach all vertices."
    ]
    fonk5(b4, 130)
    b5 = {'A': (-200, 100), 'B': (-100, 200), 'C': (0, 100), 'D': (100, 200), 'E': (200, 100),
             'F': (0, 0), 'G': (-200, -100), 'H': (-100, -200), 'I': (100, -200)}
    b6 = {
        ('A', 'B'): 8, ('A', 'H'): 7, ('B', 'C'): 11, ('B', 'I'): 9, ('C', 'D'): 2,
        ('C', 'E'): 4, ('D', 'F'): 18, ('E', 'F'): 5, ('F', 'G'): 4, ('G', 'H'): 6,
        ('H', 'I'): 15
    }
    fonk3(b5)
    fonk4(b5, b6)
    time.sleep(10)
    b7 = ['C', 'D', 'A', 'B', 'A', 'H', 'G', 'F', 'E', 'C', 'B', 'I']
    fonk6(b5, b6, b7)
if b8 = = "__main__":
    fonk7()