import turtle
import time
def draw_text(text, x, y, font=("Freestyle Script", 20, "normal"), align="center", color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(text, align=align, font=font)
def draw_edge_with_weight(start, end, weight):
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    turtle.penup()
    turtle.goto((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    turtle.write(weight, align="center", font=("Arial", 12, "normal"))
def draw_nodes(nodes):
    for node, pos in nodes.items():
        turtle.penup()
        turtle.goto(pos)
        turtle.dot(20, "green")
        draw_text(node, pos[0] + 10, pos[1] + 10, font=("Arial", 16, "normal"))
def draw_edges_with_weights(nodes, edges):
    for (start, end), weight in edges.items():
        draw_edge_with_weight(nodes[start], nodes[end], weight)
def draw_algorithm_steps(steps, y_coordinate):
    for step in steps:
        draw_text(step, 0, y_coordinate)
        y_coordinate -= 60
def animate_path(nodes, edges, path):
    turtle.pensize(15)
    turtle.fillcolor("red")
    turtle.color("red")
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        draw_edge_with_weight(nodes[start], nodes[end], edges[(start, end)])
    turtle.exitonclick()
def main():
    turtle.title("Kruskal's Algorithm")
    turtle.bgcolor("white")
    turtle.shape("turtle")
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.speed(1)
    turtle.hideturtle()
    draw_text("Kruskal's Algorithm", 0, 250, font=("Freestyle Script", 50, "normal"), color="purple")
    draw_text("Almazbek Mirlan uulu Com-17", 0, -180)
    steps = [
        "1. Sort all the edges from low weight to high",
        "2. Take the edge with the lowest weight and add it to the spanning tree.",
        "   If adding the edge created a cycle, then reject this edge.",
        "3. Keep adding edges until we reach all vertices."
    ]
    draw_algorithm_steps(steps, 130)
    nodes = {'A': (-200, 100), 'B': (-100, 200), 'C': (0, 100), 'D': (100, 200), 'E': (200, 100),
             'F': (0, 0), 'G': (-200, -100), 'H': (-100, -200), 'I': (100, -200)}
    edges = {
        ('A', 'B'): 8, ('A', 'H'): 7, ('B', 'C'): 11, ('B', 'I'): 9, ('C', 'D'): 2,
        ('C', 'E'): 4, ('D', 'F'): 18, ('E', 'F'): 5, ('F', 'G'): 4, ('G', 'H'): 6,
        ('H', 'I'): 15
    }
    draw_nodes(nodes)
    draw_edges_with_weights(nodes, edges)
    time.sleep(10)
    path = ['C', 'D', 'A', 'B', 'A', 'H', 'G', 'F', 'E', 'C', 'B', 'I']
    animate_path(nodes, edges, path)
if __name__ == "__main__":
    main()