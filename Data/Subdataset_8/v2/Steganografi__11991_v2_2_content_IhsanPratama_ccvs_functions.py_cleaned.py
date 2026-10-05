from PIL import Image
import shutil
import cv2
import os
def extract_frames(video_path):
    temp_folder = 'temp'
    try:
        os.mkdir(temp_folder)
    except FileExistsError:
        shutil.rmtree(temp_folder)
        os.mkdir(temp_folder)
    vidcap = cv2.VideoCapture(video_path)
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
        raise ValueError("The path {} does not point to a file or directory.".format(path))
def chunk_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
def caesar_cipher(char, mode, shift):
    if mode == "enc":
        ascii_val = ord(char)
        return chr((ascii_val + shift) % 128)
    elif mode == "dec":
        ascii_val = ord(char)
        return chr((ascii_val - shift) % 128)
def encode_text_into_frames(frame_dir, text_path, shift):
    with open(text_path, "r") as text_file:
        text_to_hide = repr(text_file.read())
    chunks = chunk_string(text_to_hide, 255)
    for index, chunk in enumerate(chunks):
        length = len(chunk)
        frame_path = os.path.join(frame_dir, f"{index + 1}.png")
        frame = Image.open(frame_path)
        if frame.mode != "RGB":
            print("The source frame must be in RGB format.")
            return False
        encoded_frame = frame.copy()
        width, height = frame.size
        char_index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = frame.getpixel((col, row))
                if row == 0 and col == 0 and char_index < length:
                    asc = length
                    total_encoded_frame = g
                elif char_index <= length:
                    current_char = chunk[char_index - 1]
                    asc = ord(caesar_cipher(current_char, "enc", shift))
                    total_encoded_frame = g
                else:
                    asc = r
                    total_encoded_frame = g
                encoded_frame.putpixel((col, row), (asc, total_encoded_frame, b))
                char_index += 1
        encoded_frame.save(frame_path, compress_level=0)
def decode_text_from_frames(frame_dir, shift):
    first_frame = Image.open(os.path.join(frame_dir, "1.png"))
    r, g, b = first_frame.getpixel((0, 0))
    total_encoded_frame = g
    decoded_text = ""
    for i in range(1, total_encoded_frame + 1):
        frame_path = os.path.join(frame_dir, f"{i}.png")
        frame = Image.open(frame_path)
        width, height = frame.size
        char_index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = frame.getpixel((col, row))
                except ValueError:
                    r, g, b, _ = frame.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif char_index <= length:
                    decoded_text += caesar_cipher(chr(r), "dec", shift)
                char_index += 1
    decoded_text = decoded_text[1:-1]
    with open("recovered-text.txt", "w") as recovered_txt:
        recovered_txt.write(decoded_text)
if __name__ == "__main__":
    video_file = "data/video.mp4"
    frame_dir = "frames"
    text_to_hide = "data/secret.txt"
    shift_amount = 3
    extract_frames(video_file)
    encode_text_into_frames(frame_dir, text_to_hide, shift_amount)
    decode_text_from_frames(frame_dir, shift_amount)