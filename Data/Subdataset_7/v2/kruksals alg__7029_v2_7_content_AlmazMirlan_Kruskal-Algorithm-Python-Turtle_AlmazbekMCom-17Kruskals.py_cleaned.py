import turtle
import time
def fonk1(text, x, y, b1 = ("Freestyle Script", 20, "normal"), b2="center", color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, b2 = b2, b1=b1)
def fonk2(start, b7, weight):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(b7)
    turtle.penup()
    turtle.goto((start[0] + b7[0]) / 2, (start[1] + b7[1]) / 2)
    turtle.write(weight, b2 = "center", b1=("Arial", 12, "normal"))
def fonk3():
    turtle.title("Kruskal's Algorithm")
    turtle.bgcolor("white")
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.speed(1)
    turtle.hideturtle()
    fonk1("Kruskal's Algorithm", 0, 250, b1 = ("Freestyle Script", 50, "normal"), color="purple")
    fonk1("Almazbek Mirlan uulu Com-17", 0, -180)
    b3 = [
        "1. Sort all the b5 from low weight to high",
        "2. Take the edge with the lowest weight and add it to the spanning tree.",
        "   If adding the edge created a cycle, then reject this edge.",
        "3. Keep adding b5 until we reach all vertices."
    ]
    a1 = 130
    for step in b3:
        fonk1(step, 0, a1)
        a1 -= 60
    b4 = {'A': (-200, 100), 'B': (-100, 200), 'C': (0, 100), 'D': (100, 200), 'E': (200, 100),
             'F': (0, 0), 'G': (-200, -100), 'H': (-100, -200), 'I': (100, -200)}
    for node, pos in b4.items():
        turtle.penup()
        turtle.goto(pos)
        turtle.dot(20, "green")
        fonk1(node, pos[0] + 10, pos[1] + 10, b1 = ("Arial", 16, "normal"))
    b5 = {
        ('A', 'B'): 8, ('A', 'H'): 7, ('B', 'C'): 11, ('B', 'I'): 9, ('C', 'D'): 2,
        ('C', 'E'): 4, ('D', 'F'): 18, ('E', 'F'): 5, ('F', 'G'): 4, ('G', 'H'): 6,
        ('H', 'I'): 15
    }
    for (start, b7), weight in b5.items():
        fonk2(b4[start], b4[b7], weight)
    turtle.pensize(15)
    turtle.fillcolor("red")
    turtle.color("red")
    time.sleep(10)
    b6 = ['C', 'D', 'A', 'B', 'A', 'H', 'G', 'F', 'E', 'C', 'B', 'I']
    for i in range(len(b6) - 1):
        start, b7 = b6[i], b6[i + 1]
        fonk2(b4[start], b4[b7], b5[(start, b7)])
    turtle.exitonclick()
if b8 = = "__main__":
    fonk3()