import numpy as np
import cv2
def dist((x1,y1),(x2,y2)):
    return ((x2-x1)**2+(y2-y1)**2)
def next_pos(img,bot_pos,goal):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    ret,thresh2 = cv2.threshold(gray,75,255,cv2.THRESH_BINARY_INV)
    ht,wd,ch=img.shape
    cv2.imshow('thresh',thresh2)
    cv2.waitKey(1)
    botx,boty=bot_pos[0],bot_pos[1]
    goalx,goaly=goal[0],goal[1]
    frsqrs=[(botx+20,boty),(botx-20,boty),(botx,boty+20),(botx,boty-20)]
    allow=[]
    for f in frsqrs:
        if(f[0]<ht and f[1]<wd):
            if(thresh2[f[1],f[0]]==255):
                allow.append(f)
    minallow=99999999999
    next_bot_pos=bot_pos
    for a in allow:
        distance=dist(a,goal)
        if(distance<minallow):
            minallow=distance
            next_bot_pos=a
    return (next_bot_pos,next_bot_pos[0]-bot_pos[0],next_bot_pos[1]-bot_pos[1])
if __name__=='__main__':
    img=cv2.imread('newa4.jpg')
    dict_centres={'a': (125, 110), 'c': (246, 24), 'b': (140, 285), 'e': (247, 180), 'd': (247, 110), 'g': (293, 371), 'f': (247, 269), 'i': (402, 109), 'h': (394, 287)}
    centres=[(125,110),(140,285),(246,24),(247,110),(247,180),(247,269),(293,371),(394,287),(402,109)]
    bot_pos=dict_centres['a']
    goal=dict_centres['e']
    print "goal=",goal
    cv2.imshow('image',img)
    cv2.waitKey(0) & 0xFF
    goto=bot_pos
    pos_threshold=30
    cv2.imshow('image',img)
    cv2.waitKey(100)
    cv2.imshow('final',img)
    cv2.waitKey(0)