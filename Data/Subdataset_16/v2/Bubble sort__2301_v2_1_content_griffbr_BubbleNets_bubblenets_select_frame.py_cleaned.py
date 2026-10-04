import numpy as np
import cv2
import copy
import glob
import os
import sys
b1 = os.getcwd()
sys.path.insert(0, os.path.join(b1, 'methods', 'preprocess'))
sys.path.insert(0, os.path.join(b1, 'methods', 'annotate_suggest'))
from grabCutClass import GrabCutter
from videoProcessor import VideoProcessor
from annotation_suggester import annotation_suggester
from color_hist_frame_select import color_hist_frame_select
from ResNet_preprocess import resnet_process_data_dir
from BubbleNets_frame_select import BubbleNets_sort
from BubbleNets import bn_utils
b2 = True
b3 = True
def fonk1(b32):
    b4 = os.path.basename(b32)
    print('\n\nGenerating user-guided annotation for {}'.format(b4))
    b5 = os.path.join(b32, 'usrAnnotate')
    if not os.path.isdir(b5):
        os.makedirs(b5)
    b6 = os.path.join(b32, 'src')
    b7 = sorted(glob.glob(os.path.join(b6, '*')))
    ant_idx, b8 = fonk3(os.path.join(b32, 'frame_selection', 'all.txt'))
    b9 = annotation_suggester(b32)
    b10 = True
    while b10:
        b11 = glob.glob(os.path.join(b5, '*'))
        b12 = len(b11)
        print('Currently {} annotation image(s):'.format(b12))
        for ant_file_name in b11:
            b13 = os.path.basename(ant_file_name)
            print(b13)
            if b13 in b8:
                b8.remove(b13)
        print('Suggested annotation frames remaining:')
        print(b8)
        b14 = input('Annotate another image? (y or n)\n')
        if b14.lower() not in {'y', 'yes'}:
            b10 = False
        if b10:
            while True:
                try:
                    if b3:
                        b15 = int(input('What is preferred annotation image index? ({}-{} possible)\n'.format(
                            os.path.basename(b7[0]), os.path.basename(b7[-1])))) - b9.manip_start_idx
                    else:
                        b15 = ant_idx[0]
                    b16 = b7[b15]
                    b17 = cv2.imread(b16)
                    window_x, b18 = 100, 100
                    if b2:
                        cv2.imshow('Annotation Image', b17)
                        cv2.moveWindow('Annotation Image', window_x, b18)
                        cv2.waitKey(20)
                        b19 = float(input('What is preferred b19? (e.g., 1, 2, or 0.5)\n'))
                    else:
                        b19 = 1
                    b20 = cv2.resize(b17, (0, 0), fx=b19, fy=b19)
                    cv2.imshow('Scaled Annotation Image', b20)
                    cv2.moveWindow('Scaled Annotation Image', window_x, b18)
                    cv2.waitKey(20)
                    b14 = input('Is annotation frame acceptable? (y or n)\n')
                    if b14.lower() in {'y', 'yes'}:
                        cv2.destroyAllWindows()
                        break
                except Exception as e:
                    print(f'Error: {e}. Image {b15} does not exist!')
            b21 = os.path.join(b5, os.path.basename(b16).split('.')[0] + '.png')
            GrabCutter(b16, b21, window_x, b18, b19)
            fonk2(b16, b32, b12)
def fonk2(b16, b32, annotation_frame_num):
    print('Saving extra copy of annotation image for development.')
    b22 = os.path.join(b32, 'annotation_imgs')
    if not os.path.isdir(b22):
        os.makedirs(b22)
    b23 = os.path.join(b22, '{:02d}_annotation_{}.jpg'.format(annotation_frame_num, os.path.basename(b16).split('.')[0]))
    cv2.imwrite(b23, cv2.imread(b16))
def fonk3(text_file):
    b24 = bn_utils.read_list_file(text_file)
    b25 = int(b24[0].split(' ')[0])
    ant_idx, b8 = [], []
    for i in range(b25):
        ant_idx.append(int(b24[i * 2 + 1]))
        b8.append(b24[i * 2 + 2])
    return ant_idx, b8
def fonk4():
    b26 = os.getcwd()
    b27 = os.path.join(b26, 'data')
    b28 = os.path.join(b27, 'rawData')
    b29 = sorted(next(os.walk(b28))[1])
    resnet_process_data_dir(b28)
    BubbleNets_sort(b28, b30 = 'BNLF')
    BubbleNets_sort(b28, b30 = 'BN0')
    color_hist_frame_select(b28, b31 = int(10e6))
    for b4 in b29:
        b32 = os.path.join(b28, b4)
        VideoProcessor(b32)
        fonk1(b32)
        print('Finished with {} annotation.\n\n'.format(b4))
    print('\n\nFinished with all annotations!\n\n')
if b33 = = "__main__":
    fonk4()