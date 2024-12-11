52. Repository: seanluo1/Arm-Link-AI
   File: const.py
   URL: https:
   Code Content:
b1 = "config.txt"
a1 = 3
b2 = [5, 3, 1]
b3 = (0, 0, 0)
b4 = (255, 255, 255)
b5 = (255,0,0)
b6 = (0,0,255)
b7 = '%'
b8 = 'P'
b9 = '.'
b10 = ' '
a2 = 0
a3 = 1
a4 = 2
a5 = 30
a6 = 2
   README Content:
This was one of my projects in my Artificial Intelligence course. It plays a game where you navigate around obstacles to reach a goal with the robot arm. It uses BFS to find an optimal path to the goal.
Pygame must be installed to run the game. Z and X move the first link, A and S move the second link.
To play the game, run "python mp2.py --map BasicMap --human" where BasicMap can be replaced with Map1, Map2, Map3, and Map4.
To watch the AI play the game, run "python mp2.py --map BasicMap --trajectory 1 --method bfs --granularity 1". Note that granularity is the angle that the arm moves when a key is pressed. I recommended using 1 so that the AI can navigate through tight spaces. Trajectory traces the path that the AI takes, smaller numbers will give more refined traces. Note that Map3 is unsolveable and has no possible solution.
See "Map Traces" folder for AI path examples and how the AI sees the game. The txt files show what the AI sees. '%' are obstacles, '.' are goal states, and 'P' is the start state. The first arm's angle is the x-axis, and the second arm's angel is the y-axis.
