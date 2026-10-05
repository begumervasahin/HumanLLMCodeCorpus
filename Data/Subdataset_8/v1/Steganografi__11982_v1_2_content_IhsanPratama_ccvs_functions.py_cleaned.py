from PIL import Image
import shutil
import cv2
import os
def frame_extract(video):
    temp_folder = 'temp'
    try:
        os.mkdir(temp_folder)
    except FileExistsError:
        shutil.rmtree(temp_folder)
        os.mkdir(temp_folder)
    vidcap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
def remove(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("file {} is not a file or dir.".format(path))
def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))
def caesar_ascii(char, mode, n):
    if mode == "enc":
        ascii_val = ord(char)
        return chr((ascii_val + n) % 128)
    elif mode == "dec":
        ascii_val = ord(char)
        return chr((ascii_val - n) % 128)
def encode_frame(frame_dir, text_to_hide, caesarn):
    with open(text_to_hide, "r") as text_file:
        text_to_hide = repr(text_file.read())
    text_to_hide_chopped = split2len(text_to_hide, 255)
    for chopped_text_index, text in enumerate(text_to_hide_chopped):
        length = len(text)
        frame_path = os.path.join(frame_dir, f"{chopped_text_index + 1}.png")
        frame = Image.open(frame_path)
        if frame.mode != "RGB":
            print("Source frame must be in RGB format")
            return False
        encoded = frame.copy()
        width, height = frame.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = frame.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                    total_encoded_frame = g
                elif index <= length:
                    c = text[index - 1]
                    asc = ord(caesar_ascii(c, "enc", caesarn))
                    total_encoded_frame = g
                else:
                    asc = r
                    total_encoded_frame = g
                encoded.putpixel((col, row), (asc, total_encoded_frame, b))
                index += 1
        encoded.save(frame_path, compress_level=0)
def decode_frame(frame_dir, caesarn):
    first_frame = Image.open(os.path.join(frame_dir, "1.png"))
    r, g, b = first_frame.getpixel((0, 0))
    total_encoded_frame = g
    msg = ""
    for i in range(1, total_encoded_frame + 1):
        frame_path = os.path.join(frame_dir, f"{i}.png")
        frame = Image.open(frame_path)
        width, height = frame.size
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = frame.getpixel((col, row))
                except ValueError:
                    r, g, b, _ = frame.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += caesar_ascii(chr(r), "dec", caesarn)
                index += 1
    msg = msg[1:-1]
    with open("recovered-text.txt", "w") as recovered_txt:
        recovered_txt.write(msg)
if __name__ == "__main__":
    video_file = "data/video.mp4"
    frame_dir = "frames"
    text_to_hide = "data/secret.txt"
    caesarn = 3
    frame_extract(video_file)
    encode_frame(frame_dir, text_to_hide, caesarn)
    decode_frame(frame_dir, caesarn)