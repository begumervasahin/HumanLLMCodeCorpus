import numpy as np
import cv2
import os
import sys
import glob
from grabCutClass import GrabCutter
from videoProcessor import VideoProcessor
from annotation_suggester import annotation_suggester
from color_hist_frame_select import color_hist_frame_select
from ResNet_preprocess import resnet_process_data_dir
from BubbleNets_frame_select import BubbleNets_sort
from BubbleNets import bn_utils
b1 = os.getcwd()
sys.path.insert(0, os.path.join(b1, 'methods', 'preprocess'))
sys.path.insert(0, os.path.join(b1, 'methods', 'annotate_suggest'))
b2 = True
b3 = True
def fonk1(b33):
    b4 = os.path.basename(b33)
    print(f'\n\nGenerating user-guided annotation for {b4}')
    b5 = os.path.join(b33, 'usrAnnotate')
    os.makedirs(b5, b6 = True)
    b7 = os.path.join(b33, 'src')
    b8 = sorted(glob.glob(os.path.join(b7, '*')))
    b26, b9 = fonk5(os.path.join(b33, 'frame_selection', 'all.txt'))
    b10 = annotation_suggester(b33)
    b11 = True
    while b11:
        b12 = glob.glob(os.path.join(b5, '*'))
        b13 = len(b12)
        print(f'Currently {b13} annotation image(s):')
        for ant_file_name in b12:
            b14 = os.path.basename(ant_file_name)
            print(b14)
            if b14 in b9:
                b9.remove(b14)
        print('Suggested annotation frames remaining:')
        print(b9)
        b15 = input('Annotate another image? (y or n)\n')
        if b15.lower() not in {'y', 'yes'}:
            b11 = False
        if b11:
            while True:
                try:
                    b16 = fonk2(b8, b10)
                    b17 = b8[b16]
                    b18 = cv2.imread(b17)
                    b19 = fonk3(b18) if b2 else 1
                    b20 = cv2.resize(b18, (0, 0), fx=b19, fy=b19)
                    cv2.imshow('Scaled Annotation Image', b20)
                    cv2.moveWindow('Scaled Annotation Image', 100, 100)
                    cv2.waitKey(20)
                    b15 = input('Is annotation frame acceptable? (y or n)\n')
                    if b15.lower() in {'y', 'yes'}:
                        cv2.destroyAllWindows()
                        break
                except Exception as e:
                    print(f'Error: {e}. Image {b16} does not exist!')
            b21 = os.path.join(b5, f"{os.path.basename(b17).split('.')[0]}.png")
            GrabCutter(b17, b21, 100, 100, b19)
            fonk4(b17, b33, b13)
def fonk2(b8, b10):
    if b3:
        return int(input(f'What is preferred annotation image index? ({os.path.basename(b8[0])}-{os.path.basename(b8[-1])} possible)\n')) - b10.manip_start_idx
    return b10.suggest_frame()
def fonk3(b18):
    cv2.imshow('Annotation Image', b18)
    cv2.moveWindow('Annotation Image', 100, 100)
    cv2.waitKey(20)
    return float(input('What is preferred b19? (e.g., 1, 2, or 0.5)\n'))
def fonk4(b17, b33, annotation_frame_num):
    print('Saving extra copy of annotation image for development.')
    b22 = os.path.join(b33, 'annotation_imgs')
    os.makedirs(b22, b6 = True)
    b23 = os.path.join(b22, f"{annotation_frame_num:02d}_annotation_{os.path.basename(b17).split('.')[0]}.jpg")
    cv2.imwrite(b23, cv2.imread(b17))
def fonk5(text_file):
    b24 = bn_utils.read_list_file(text_file)
    b25 = int(b24[0].split(' ')[0])
    b26 = [int(b24[i * 2 + 1]) for i in range(b25)]
    b9 = [b24[i * 2 + 2] for i in range(b25)]
    return b26, b9
def fonk6():
    b27 = os.getcwd()
    b28 = os.path.join(b27, 'data')
    b29 = os.path.join(b28, 'rawData')
    b30 = sorted(next(os.walk(b29))[1])
    resnet_process_data_dir(b29)
    BubbleNets_sort(b29, b31 = 'BNLF')
    BubbleNets_sort(b29, b31 = 'BN0')
    color_hist_frame_select(b29, b32 = int(10e6))
    for b4 in b30:
        b33 = os.path.join(b29, b4)
        VideoProcessor(b33)
        fonk1(b33)
        print(f'Finished with {b4} annotation.\n\n')
    print('\n\nFinished with all annotations!\n\n')
if b34 = = "__main__":
    fonk6()