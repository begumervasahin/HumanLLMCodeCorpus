import turtle
import time
def setup_turtle():
    turtle.title("Kruskal's Algorithm")
    turtle.bgcolor("white")
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.hideturtle()
    turtle.speed(1)
    turtle.penup()
def write_text(content, align="center", font=("Freestyle Script", 20, "normal"), angle=0):
    turtle.write(content, align=align, font=font)
    turtle.left(angle)
def draw_edges_and_labels():
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    edges = [("A", "B", 8), ("B", "C", 11), ("C", "D", 2), ("D", "E", 2),
             ("E", "F", 4), ("F", "G", 5), ("G", "H", 6), ("H", "A", 7),
             ("B", "I", 9), ("I", "D", 12), ("I", "H", 15), ("I", "F", 18)]
    turtle.color("black")
    for label in labels:
        turtle.dot(20, "green")
        turtle.write(label, font=("Arial", 16, "normal"))
        turtle.fd(100)
    turtle.right(180)
    for edge in edges:
        turtle.fd(edge[2])
        turtle.dot(20, "green")
        turtle.write(f"   {edge[2]}", font=("Arial", 16, "normal"))
        turtle.fd(40)
def highlight_minimum_spanning_tree():
    edges = [(0, 7), (7, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (1, 8)]
    turtle.pensize(15)
    turtle.fillcolor("red")
    turtle.color("red")
    for edge in edges:
        turtle.right(90)
        turtle.fd(163)
        turtle.dot(10, "red")
        turtle.right(90)
        turtle.fd(203)
        turtle.dot(10, "red")
def main():
    setup_turtle()
    write_text("Kruskal's Algorithm", font=("Freestyle Script", 50, "normal"))
    write_text("Almazbek Mirlan uulu Com-17", angle=45)
    write_text("Kruskal's Algorithm is one of the greedy algorithms to find the minimum spanning tree of a graph.", angle=90)
    write_text("A spanning tree is a subgraph that contains all the vertices of the original graph.", angle=90)
    write_text("The steps for implementing Kruskal's algorithm are as follows:", angle=90)
    write_text("1. Sort all the edges from low weight to high.", angle=90)
    write_text("2. Take the edge with the lowest weight and add it to the spanning tree.", angle=90)
    write_text("   If adding the edge creates a cycle, then reject this edge.", angle=90)
    write_text("3. Keep adding edges until we reach all vertices.", angle=90)
    draw_edges_and_labels()
    highlight_minimum_spanning_tree()
    turtle.exitonclick()
if __name__ == "__main__":
    main()