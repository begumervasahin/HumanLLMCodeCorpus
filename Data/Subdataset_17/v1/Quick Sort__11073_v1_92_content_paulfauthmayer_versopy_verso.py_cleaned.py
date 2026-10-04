import argparse
import logging
import sys
from pathlib import Path
from collections import Counter
import cv2
import numpy as np
import yaml
from natsort import natsorted
KEY_CANCEL = 'q'
VALID_IMG_SUFFIXES = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
def decide_image(img, options):
    cond = True
    while cond:
        cv2.imshow('IMG', img)
        choice = cv2.waitKey(0)
        choice = chr(choice & 255)
        if choice in [*options, KEY_CANCEL]:
            cond = False
    cv2.destroyAllWindows()
    return choice
def main(args):
    size = 512
    img_container = []
    for path in args.img_paths:
        images = [
            img for img in path.iterdir()
            if img.suffix.lower() in VALID_IMG_SUFFIXES
        ]
        img_container.append(images)
    flattened = [img for img_list in img_container for img in img_list]
    counts = Counter([img.name for img in flattened])
    kept = [name for name in counts if counts[name] <= len(img_container)]
    discarded = [name for name in counts if counts[name] < len(img_container)]
    for img in discarded:
        print(f'image {img} only found in {counts[img]}/{len(img_container)} lists and is skipped')
    img_container = [
        natsorted([
            img for img in img_list
            if img.name in kept
        ])
        for img_list in img_container
    ]
    img_tuples = zip(*img_container)
    choices = {key: [] for key in args.choices}
    for images in img_tuples:
        try:
            img_show = []
            for img_name in images:
                img = cv2.imread(str(img_name))
                img = cv2.resize(img, (size, size))
                img_show.append(img)
            img_show = np.concatenate(img_show, axis=1)
            choice = decide_image(img_show, args.choices)
            if choice == KEY_CANCEL:
                break
            else:
                choices[choice] += [str(img_name) for img_name in images]
        except Exception as e:
            print(e)
    if args.output:
        with open(args.output, 'w') as f:
            yaml.dump(choices, f)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'img_paths',
        type=Path,
        nargs='+',
        help='Paths to directories containing images'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output YAML file to save the choices'
    )
    parser.add_argument(
        '--choices',
        nargs='+',
        default=['s', 'd', 'k'],
        help='List of choices for categorizing images'
    )
    args = parser.parse_args()
    main(args)