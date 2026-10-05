import numpy as np
import cv2
import glob
import os
from grabCutClass import GrabCutter
from annotation_suggester import AnnotationSuggester
from BubbleNets_frame_select import BubbleNets_sort
from ResNet_preprocess import resnet_process_data_dir
from color_hist_frame_select import color_hist_frame_select
from videoProcessor import VideoProcessor
from BubbleNets import bn_utils
b1 = True
b2 = True
def fonk1(b29):
    b3 = os.path.basename(b29)
    print(f"\n\nGenerating user-guided annotation for {b3}.\n")
    b4 = os.path.join(b29, 'usrAnnotate')
    if not os.path.isdir(b4):
        os.makedirs(b4)
    b5 = os.path.join(b29, 'src')
    b6 = sorted(glob.glob(os.path.join(b5, '*')))
    b22, b7 = fonk3(os.path.join(b29, 'frame_selection', 'all.txt'))
    b8 = AnnotationSuggester(b29)
    b9 = True
    while b9:
        b10 = sorted(glob.glob(os.path.join(b4, '*')))
        b11 = len(b10)
        print(f"Currently {b11} annotation image(s):")
        for ant_img_file in b10:
            print(os.path.basename(ant_img_file))
            if os.path.basename(ant_img_file) in b7:
                del b7[b7.index(os.path.basename(ant_img_file))]
        print('Suggested annotation frames remaining:')
        print(b7)
        b12 = input('Annotate another image? (y or n)\n')
        if b12.lower() not in {'y', 'yes'}:
            b9 = False
        if b9:
            while True:
                if b2:
                    b13 = int(input(f"What is the preferred annotation image index? "
                                                      f"({os.path.basename(b6[0])}-"
                                                      f"{os.path.basename(b6[-1])} possible)\n"))
                    b13 -= b8.manip_start_idx
                else:
                    b13 = b22[0]
                try:
                    b5 = b6[b13]
                    b14 = cv2.imread(b5)
                    window_x, b15 = 100, 100
                    if b1:
                        cv2.imshow('Annotation Image', b14)
                        cv2.moveWindow('Annotation Image', window_x, b15)
                        cv2.waitKey(20)
                        b16 = float(input('What is the preferred b16? (e.g., 1, 2, or 0.5)\n'))
                    else:
                        b16 = 1
                    b17 = cv2.resize(b14, (0, 0), fx=b16, fy=b16)
                    cv2.imshow('Scaled Annotation Image', b17)
                    cv2.moveWindow('Scaled Annotation Image', window_x, b15)
                    cv2.waitKey(20)
                    b12 = input('Is the annotation frame acceptable? (y or n)\n')
                    if b12.lower() in {'y', 'yes'}:
                        cv2.destroyAllWindows()
                        break
                except Exception as e:
                    print(f"Error: {e}")
            b18 = os.path.join(b4, os.path.basename(b5).split('.')[0] + '.png')
            GrabCutter(b5, b18, window_x, b15, b16)
            fonk2(b5, b29, b11)
def fonk2(b5, b29, annotation_frame_num):
    print('Saving an extra copy of the annotation image for development.')
    b19 = os.path.join(b29, 'annotation_imgs')
    if not os.path.isdir(b19):
        os.makedirs(b19)
    cv2.imwrite(os.path.join(b19, format(annotation_frame_num, '02d')
                             + '_annotation_' + os.path.basename(b5).split('.')[0] + '.jpg'),
                cv2.imread(b5))
def fonk3(text_file):
    b20 = bn_utils.read_list_file(text_file)
    b21 = int(b20[0].split(' ')[0])
    b22 = [int(b20[i * 2 + 1]) for i in range(b21)]
    b7 = [b20[i * 2 + 2] for i in range(b21)]
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
    for b3 in b26:
        b29 = os.path.join(b25, b3)
        VideoProcessor(b29)
        fonk1(b29)
        print(f'Finished with {b3} annotation.\n\n')
    print('\n\nFinished with all annotations!\n\n')
if b30 = = "__main__":
    fonk4()