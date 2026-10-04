import os
import csv
import base64
import numpy as np
import http.client
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
pics = {}
def read_from_csv(csv_dir='./csv'):
    for filename in os.listdir(csv_dir):
        filepath = os.path.join(csv_dir, filename)
        with open(filepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                image_name, vector_str = row[1], row[2]
                vector = np.fromstring(vector_str[1:-1], dtype=np.float_, sep=' ')
                pics[image_name] = vector
def add_image_vector(pic_rel_path):
    img2vec = Img2Vec()
    filename = os.fsdecode(pic_rel_path)
    print(f"Processing file: {filename}")
    img = Image.open(filename)
    vec = img2vec.get_vec(img)
    pics[filename] = vec
def search_offline():
    pic_rel_path = input("Enter the relative path of the image to search:\n")
    add_image_vector(pic_rel_path)
    read_from_csv()
    try:
        target_vector = pics[pic_rel_path]
        similarities = {}
        for key, vec in pics.items():
            if key == pic_rel_path:
                continue
            similarity = cosine_similarity(target_vector.reshape((1, -1)), vec.reshape((1, -1)))[0][0]
            similarities[key] = similarity
        sorted_similarities = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
        for similarity, filename in sorted_similarities[:5]:
            print(f"Similarity: {similarity:.4f}, Filename: {filename}")
    except KeyError:
        print(f'Filename {pic_rel_path} not found in the dictionary.')
    except Exception as e:
        print(f"An error occurred: {e}")
def search_online():
    pic_rel_path = input("Enter the relative path of the image to search:\n")
    with open(pic_rel_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    conn = http.client.HTTPConnection("beard-app.herokuapp.com")
    headers = {'Content-Type': "text/plain"}
    conn.request("PUT", "/image_clustering", encoded_string, headers)
    response = conn.getresponse()
    data = response.read()
    print(data.decode("utf-8"))
if __name__ == '__main__':
    search_online()