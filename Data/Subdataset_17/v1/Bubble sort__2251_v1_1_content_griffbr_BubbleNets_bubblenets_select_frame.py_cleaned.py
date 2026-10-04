import numpy as np
import cv2
import IPython
import copy
import glob
import os
import sys
cwd = os.getcwd()
sys.path.insert(0, os.path.join(cwd, 'methods', 'preprocess'))
sys.path.insert(0, os.path.join(cwd, 'methods', 'annotate_suggest'))
from grabCutClass import GrabCutter
from videoProcessor import VideoProcessor
from annotation_suggester import annotation_suggester
from color_hist_frame_select import color_hist_frame_select
from ResNet_preprocess import resnet_process_data_dir
from BubbleNets_frame_select import BubbleNets_sort
from BubbleNets import bn_utils
user_scale = True
user_select = True
def get_user_annotation(videoDir):
    videoName = os.path.basename(videoDir)
    print('\n\nGenerating user-guided annotation for {}'.format(videoName))
    annotationDir = os.path.join(videoDir, 'usrAnnotate')
    if not os.path.isdir(annotationDir):
        os.makedirs(annotationDir)
    imageDir = os.path.join(videoDir, 'src')
    imageFiles = sorted(glob.glob(os.path.join(imageDir, '*')))
    ant_idx, ant_file = read_annotation_list(os.path.join(videoDir, 'frame_selection', 'all.txt'))
    suggester = annotation_suggester(videoDir)
    userAnnotating = True
    while userAnnotating:
        antImageFiles = glob.glob(os.path.join(annotationDir, '*'))
        nAntImgs = len(antImageFiles)
        print('Currently {} annotation image(s):'.format(nAntImgs))
        for i in range(nAntImgs):
            ant_name = os.path.basename(antImageFiles[i])
            print(ant_name)
            if ant_name in ant_file:
                ant_file.remove(ant_name)
        print('Suggested annotation frames remaining:')
        print(ant_file)
        response = input('Annotate another image? (y or n)\n')
        if response.lower() not in {'y', 'yes'}:
            userAnnotating = False
        if userAnnotating:
            while True:
                try:
                    if user_select:
                        annotationImageIdx = int(input('What is preferred annotation image index? ({}-{} possible)\n'.format(
                            os.path.basename(imageFiles[0]), os.path.basename(imageFiles[-1])))) - suggester.manip_start_idx
                    else:
                        annotationImageIdx = ant_idx[0]
                    imageDir = imageFiles[annotationImageIdx]
                    annotationImage = cv2.imread(imageDir)
                    windowx, windowy = 100, 100
                    if user_scale:
                        cv2.imshow('Annotation Image', annotationImage)
                        cv2.moveWindow('Annotation Image', windowx, windowy)
                        cv2.waitKey(20)
                        scale = float(input('What is preferred scale? (e.g., 1, 2, or 0.5)\n'))
                    else:
                        scale = 1
                    annotationImageScaled = cv2.resize(annotationImage, (0, 0), fx=scale, fy=scale)
                    cv2.imshow('Scaled Annotation Image', annotationImageScaled)
                    cv2.moveWindow('Scaled Annotation Image', windowx, windowy)
                    cv2.waitKey(20)
                    response = input('Is annotation frame acceptable? (y or n)\n')
                    if response.lower() in {'y', 'yes'}:
                        cv2.destroyAllWindows()
                        break
                except:
                    print('Image {} does not exist!'.format(annotationImageIdx))
            outputMaskDir = os.path.join(annotationDir, os.path.basename(imageDir).split('.')[0] + '.png')
            GrabCutter(imageDir, outputMaskDir, windowx, windowy, scale)
            save_extra_image_copy(imageDir, videoDir, nAntImgs)
def save_extra_image_copy(image_dir, video_dir, annotation_frame_num):
    print('Saving extra copy of annotation image for development.')
    extra_image_dir = os.path.join(video_dir, 'annotation_imgs')
    if not os.path.isdir(extra_image_dir):
        os.makedirs(extra_image_dir)
    cv2.imwrite(os.path.join(extra_image_dir, '{:02d}_annotation_{}.jpg'.format(annotation_frame_num, os.path.basename(image_dir).split('.')[0])),
                cv2.imread(image_dir))
def read_annotation_list(text_file):
    read_list = bn_utils.read_list_file(text_file)
    n_ant = int(read_list[0].split(' ')[0])
    ant_idx, ant_file = [], []
    for i in range(n_ant):
        ant_idx.append(int(read_list[i * 2 + 1]))
        ant_file.append(read_list[i * 2 + 2])
    return ant_idx, ant_file
def main():
    mainDir = os.getcwd()
    dataDir = os.path.join(mainDir, 'data')
    rawDataDir = os.path.join(dataDir, 'rawData')
    videoList = sorted(next(os.walk(rawDataDir))[1])
    resnet_process_data_dir(rawDataDir)
    BubbleNets_sort(rawDataDir, model='BNLF')
    BubbleNets_sort(rawDataDir, model='BN0')
    color_hist_frame_select(rawDataDir, annotate_rate=int(10e6))
    for videoName in videoList:
        videoDir = os.path.join(rawDataDir, videoName)
        VideoProcessor(videoDir)
        get_user_annotation(videoDir)
        print('Finished with {} annotation.\n\n'.format(videoName))
    print('\n\nFinished with all annotations!\n\n')
if __name__ == "__main__":
    main()