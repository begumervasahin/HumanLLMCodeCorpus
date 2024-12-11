import numpy as np
import cv2
import os
import glob
import sys
from methods.preprocess.grabCutClass import GrabCutter
from methods.preprocess.videoProcessor import VideoProcessor
from methods.annotate_suggest.annotation_suggester import annotation_suggester
from methods.preprocess.color_hist_frame_select import color_hist_frame_select
from methods.preprocess.ResNet_preprocess import resnet_process_data_dir
from methods.preprocess.BubbleNets_frame_select import BubbleNets_sort
from methods.BubbleNets import bn_utils
b1 = True
b2 = True
def fonk1(b29):
    b3 = os.path.basename(b29)
    print(f"\n\nGenerating user-guided annotation for {b3}.\n")
    b4 = os.path.join(b29, 'usrAnnotate')
    if not os.path.isdir(b4):
        os.makedirs(b4)
    b5 = os.path.join(b29, 'src')
    b6 = glob.glob(os.path.join(b5,'*'))
    b6.sort()
    b22, b7 = fonk3(os.path.join(b29,'frame_selection','all.txt'))
    b8 = annotation_suggester(b29)
    b9 = True
    while b9:
        b10 = glob.glob(os.path.join(b4,'*'))
        b11 = len(b10)
        print(f"Currently {b11} annotation image(s):")
        for i in range(0, b11):
            b12 = os.path.basename(b10[i])
            print(b12)
            if b12 in b7:
                del b7[b7.index(b12)]
        print('Suggested annotation frames remaining:')
        print(b7)
        b13 = input('Annotate another image? (y or n)\n')
        if b13.lower() not in {'y', 'yes'}:
            b9 = False
        if b9:
            while True:
                if b2:
                    b14 = int(input(f'What is preferred annotation image index? ({os.path.basename(b6[0])}-{os.path.basename(b6[-1])} possible)\n'))
                    b14 -= b8.manip_start_idx
                else:
                    b14 = b22[0]
                try:
                    b5 = b6[int(b14)]
                    b15 = cv2.imread(b5)
                    a1 = 100
                    a2 = 100
                    if b1:
                        cv2.imshow('Annotation Image', b15)
                        cv2.moveWindow('Annotation Image', a1, a2)
                        cv2.waitKey(20)
                        b16 = float(input('What is preferred b16? (e.g., 1, 2, or 0.5)\n'))
                    else:
                        b16 = 1
                    b17 = cv2.resize(b15, (0,0), fx=b16, fy=b16)
                    cv2.imshow('Scaled Annotation Image', b17)
                    cv2.moveWindow('Scaled Annotation Image', a1, a2)
                    cv2.waitKey(20)
                    b13 = input('Is annotation frame acceptable? (y or n)\n')
                    if b13.lower() in {'y', 'yes'}:
                        cv2.destroyAllWindows()
                        break
                except:
                    print(f'Image {b14} does not exist!')
            b18 = os.path.join(b4, os.path.basename(b5).split('.')[0] + '.png')
            GrabCutter(b5, b18, a1, a2, b16)
            fonk2(b5, b29, b11)
def fonk2(image_dir, video_dir, annotation_frame_num):
    print('Saving extra copy of annotation image for development.')
    b19 = os.path.join(video_dir, 'annotation_imgs')
    if not os.path.isdir(b19):
        os.makedirs(b19)
    cv2.imwrite(os.path.join(b19, f"{annotation_frame_num:02d}_annotation_{os.path.basename(image_dir).split('.')[0]}.jpg"),
                cv2.imread(image_dir))
def fonk3(text_file):
    b20 = bn_utils.read_list_file(text_file)
    b21 = int(b20[0].split(' ')[0])
    b22 = []
    b7 = []
    for i in range(b21):
        b22.append(int(b20[i * 2 + 1]))
        b7.append(b20[i * 2 + 2])
    return b22, b7
def fonk4():
    b23 = os.getcwd()
    b24 = os.path.join(b23, 'data')
    b25 = os.path.join(b24, 'rawData')
    b26 = sorted(next(os.walk(b25))[1])
    resnet_process_data_dir(b25)
    BubbleNets_sort(b25, b27 = 'BNLF')
    BubbleNets_sort(b25, b27 = 'BN0')
    color_hist_frame_select(b25, b28 = int(10e6))
    for i, b3 in enumerate(b26):
        b29 = os.path.join(b25, b3)
        VideoProcessor(b29)
        fonk1(b29)
        print(f'Finished with {b3} annotation.\n\n')
    print('\n\nFinished with all annotations!\n\n')
if b30 = = "__main__":
    fonk4()