import turtle
import time
def fonk1():
    turtle.title("Kruskal's Algorithm")
    turtle.bgcolor("white")
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.hideturtle()
    turtle.speed(1)
    turtle.penup()
def fonk2(content, b1 = "center", b4=("Freestyle Script", 20, "normal"), b5=0):
    turtle.write(content, b1 = b1, b4=b4)
    turtle.left(b5)
def fonk3():
    b2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    b3 = [("A", "B", 8), ("B", "C", 11), ("C", "D", 2), ("D", "E", 2),
             ("E", "F", 4), ("F", "G", 5), ("G", "H", 6), ("H", "A", 7),
             ("B", "I", 9), ("I", "D", 12), ("I", "H", 15), ("I", "F", 18)]
    turtle.color("black")
    for label in b2:
        turtle.dot(20, "green")
        turtle.write(label, b4 = ("Arial", 16, "normal"))
        turtle.fd(100)
    turtle.right(180)
    for edge in b3:
        turtle.fd(edge[2])
        turtle.dot(20, "green")
        turtle.write(f"   {edge[2]}", b4 = ("Arial", 16, "normal"))
        turtle.fd(40)
def fonk4():
    b3 = [(0, 7), (7, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 8)]
    turtle.pensize(15)
    turtle.fillcolor("red")
    turtle.color("red")
    for edge in b3:
        turtle.right(90)
        turtle.fd(163)
        turtle.dot(10, "red")
        turtle.right(90)
        turtle.fd(203)
        turtle.dot(10, "red")
def fonk5():
    fonk1()
    fonk2("Kruskal's Algorithm", b4 = ("Freestyle Script", 50, "normal"))
    fonk2("Almazbek Mirlan uulu Com-17", b5 = 45)
    fonk2("Kruskal's Algorithm is one of the greedy algorithms to find the minimum spanning tree of a graph.", b5 = 90)
    fonk2("A spanning tree is a subgraph that contains all the vertices of the original graph.", b5 = 90)
    fonk2("The steps for implementing Kruskal's algorithm are as follows:", b5 = 90)
    fonk2("1. Sort all the b3 from low weight to high.", b5 = 90)
    fonk2("2. Take the edge with the lowest weight and add it to the spanning tree.", b5 = 90)
    fonk2("   If adding the edge creates a cycle, then reject this edge.", b5 = 90)
    fonk2("3. Keep adding b3 until we reach all vertices.", b5 = 90)
    fonk3()
    fonk4()
    turtle.exitonclick()
if b6 = = "__main__":
    fonk5()