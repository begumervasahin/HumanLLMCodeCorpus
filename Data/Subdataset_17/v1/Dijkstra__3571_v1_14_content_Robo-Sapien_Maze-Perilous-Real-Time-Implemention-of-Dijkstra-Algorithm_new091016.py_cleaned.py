import numpy as np
import cv2
def dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2
def next_pos(img, bot_pos, goal):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)
    ret, thresh2 = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY_INV)
    ht, wd, _ = img.shape
    cv2.imshow('Threshold Image', thresh2)
    cv2.waitKey(1)
    botx, boty = bot_pos
    goalx, goaly = goal
    frsqrs = [(botx + 20, boty), (botx - 20, boty), (botx, boty + 20), (botx, boty - 20)]
    allow = []
    for f in frsqrs:
        if 0 <= f[0] < ht and 0 <= f[1] < wd:
            if thresh2[f[1], f[0]] == 255:
                allow.append(f)
    minallow = float('inf')
    next_bot_pos = bot_pos
    for a in allow:
        distance = dist(a, goal)
        if distance < minallow:
            minallow = distance
            next_bot_pos = a
    return next_bot_pos, next_bot_pos[0] - bot_pos[0], next_bot_pos[1] - bot_pos[1]
if __name__ == '__main__':
    img = cv2.imread('newa4.jpg')
    dict_centres = {
        'a': (125, 110), 'c': (246, 24), 'b': (140, 285), 'e': (247, 180),
        'd': (247, 110), 'g': (293, 371), 'f': (247, 269), 'i': (402, 109), 'h': (394, 287)
    }
    centres = [(125, 110), (140, 285), (246, 24), (247, 110), (247, 180), (247, 269), (293, 371), (394, 287), (402, 109)]
    bot_pos = dict_centres['a']
    goal = dict_centres['e']
    print("Goal:", goal)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    goto = bot_pos
    pos_threshold = 30
    while dist(goto, goal) > pos_threshold:
        goto, dx, dy = next_pos(img, goto, goal)
        bot_pos = (bot_pos[0] + dx, bot_pos[1] + dy)
        print(f"Bot Position: {bot_pos}")
        cv2.circle(img, bot_pos, 5, (0, 0, 255), -1)
        cv2.imshow('Path', img)
        cv2.waitKey(100)
    cv2.imshow('Final Path', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()