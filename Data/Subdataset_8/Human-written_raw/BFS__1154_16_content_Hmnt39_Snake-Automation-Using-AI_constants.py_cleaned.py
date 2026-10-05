16. Repository: Hmnt39/Snake-Automation-Using-AI
   File: constants.py
   URL: https:
   Code Content:
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
GRAY      = ( 20,  20,  20)
BGCOLOR = BLACK
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0
w = 400
h = 400
block_size = 40
width = int(w / block_size)
height = int(h / block_size)
   README Content:
![Image of Snake Game](https:
Automation of classic Snake game using general and domain specific algorithms in Artificial Intelligence like BFS, Neural Networks,
Hamiltonian etc.
This project aims to explore different algorithms which play the game by themselves i.e. essentially making an AI that plays Snake.
When playing the game, there is a decision to make each time the snake takes a step forward: continue straight, turn left, or turn right.
Our goal is to create an AI to learn how to make this same decision. First assessing the state of the world that the snake lives in,
then choosing the move that will keep it alive and continue to grow longer.
Furthermore, this project compares the performance of each algorithm and created graph of Scores versus Number of games played and
deduce the average score to find better algorithm.
  ![Image of BFS](https:
  ![Image of neural](https:
Performance of algorithms (average score vs algorithm)
  ![Image of Performance](https:
