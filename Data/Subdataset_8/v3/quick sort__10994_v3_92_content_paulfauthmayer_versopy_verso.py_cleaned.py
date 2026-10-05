import argparse
from collections import Counter
from pathlib import Path
import cv2
import numpy as np
import yaml
from natsort import natsorted
from constants import KEY_CANCEL, VALID_IMG_SUFFIXES
def decide_image(img, options):
    cond = True
    while cond:
        cv2.imshow('IMG', img)
        choice = cv2.waitKey(0)
        choice = chr(choice & 255)
        if choice in options or choice == KEY_CANCEL:
            cond = False
    return choice
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('img_paths', type=Path, nargs='+', help='Paths to image directories')
    parser.add_argument('--output', type=Path, help='Path to output YAML file')
    parser.add_argument('--choices', nargs='+', default=['s', 'd', 'k'], help='List of choices for user')
    args = parser.parse_args()
    size = 512
    img_container = []
    for path in args.img_paths:
        images = [img for img in path.iterdir() if img.suffix in VALID_IMG_SUFFIXES]
        img_container.append(images)
    flattened = [img for img_list in img_container for img in img_list]
    counts = Counter([img.name for img in flattened])
    kept = [name for name in counts if counts[name] <= len(img_container)]
    discarded = [name for name in counts if counts[name] < len(img_container)]
    for img in discarded:
        print(f'Image {img} only found in {counts[img]}/{len(img_container)} lists and is skipped')
    img_container = [natsorted([img for img in img_list if img.name in kept]) for img_list in img_container]
    img_tuples = zip(*img_container)
    choices = {key: [] for key in args.choices}
    for i, images in enumerate(img_tuples):
        try:
            img_show = [cv2.resize(cv2.imread(str(img_name)), (size, size)) for img_name in images]
            img_show = np.concatenate(img_show, axis=1)
            choice = decide_image(img_show, args.choices)
            if choice == KEY_CANCEL:
                break
            else:
                choices[choice] += [str(img_name)]
        except Exception as e:
            print(e)
    if args.output:
        with open(args.output, 'w') as f:
            yaml.dump(choices, f)