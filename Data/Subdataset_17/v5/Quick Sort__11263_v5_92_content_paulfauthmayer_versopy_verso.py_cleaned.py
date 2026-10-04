import argparse
import logging
import sys
from pathlib import Path
from collections import Counter
import cv2
import numpy as np
import yaml
from natsort import natsorted
from constants import KEY_CANCEL, VALID_IMG_SUFFIXES
def decide_image(img, options):
    while True:
        cv2.imshow('IMG', img)
        choice = chr(cv2.waitKey(0) & 255)
        if choice in options or choice == KEY_CANCEL:
            break
    return choice
def parse_arguments():
    parser = argparse.ArgumentParser(description="Process images and collect user choices.")
    parser.add_argument(
        'img_paths',
        type=Path,
        nargs='+',
        help='Paths to directories containing images.'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Path to output YAML file.'
    )
    parser.add_argument(
        '--choices',
        nargs='+',
        default=['s', 'd', 'k'],
        help='List of choices for user input.'
    )
    return parser.parse_args()
def load_images(paths):
    img_container = []
    for path in paths:
        images = [img for img in path.iterdir() if img.suffix.lower() in VALID_IMG_SUFFIXES]
        img_container.append(images)
    return img_container
def filter_images(img_container):
    flattened = [img for img_list in img_container for img in img_list]
    counts = Counter(img.name for img in flattened)
    kept = {name for name in counts if counts[name] == len(img_container)}
    discarded = {name for name in counts if counts[name] < len(img_container)}
    for img in discarded:
        logging.info(f'image {img} only found in {counts[img]}/{len(img_container)} lists and is skipped')
    return [
        natsorted([img for img in img_list if img.name in kept])
        for img_list in img_container
    ]
def process_images(img_tuples, choices, size):
    result = {key: [] for key in choices}
    for images in img_tuples:
        try:
            img_show = [cv2.resize(cv2.imread(str(img)), (size, size)) for img in images]
            img_show = np.concatenate(img_show, axis=1)
            choice = decide_image(img_show, choices)
            if choice == KEY_CANCEL:
                break
            result[choice].extend(str(img) for img in images)
        except Exception as e:
            logging.error(f"Error processing images: {e}")
    return result
def main():
    args = parse_arguments()
    img_container = load_images(args.img_paths)
    img_container = filter_images(img_container)
    img_tuples = zip(*img_container)
    choices = process_images(img_tuples, args.choices, size=512)
    if args.output:
        with open(args.output, 'w') as f:
            yaml.dump(choices, f)
if __name__ == '__main__':
    main()