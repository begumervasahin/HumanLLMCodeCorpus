from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
import numpy as np
import http.client
import os
import csv
import base64
image_vectors = {}
def read_image_vectors_from_csv():
    csv_dir = './csv'
    for filename in os.listdir(csv_dir):
        with open(os.path.join(csv_dir, filename), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                image_vectors[row[1]] = np.fromstring(row[2][1:-1], dtype=np.float_, sep=' ')
def extract_and_store_image_vector(image_rel_path):
    img2vec = Img2Vec()
    filename = os.fsdecode(image_rel_path)
    print("Processing image:", filename)
    img = Image.open(os.path.join('.', filename))
    vec = img2vec.get_vec(img)
    image_vectors[filename] = vec
def search_offline():
    image_rel_path = input("Enter the relative path of the image to search:\n")
    extract_and_store_image_vector(image_rel_path)
    read_image_vectors_from_csv()
    try:
        query_vector = image_vectors[image_rel_path]
        similarities = {}
        for key, vector in image_vectors.items():
            if key == image_rel_path:
                continue
            similarity = cosine_similarity(query_vector.reshape(1, -1), vector.reshape(1, -1))[0][0]
            similarities[key] = similarity
        sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        print("Top 5 similar images:")
        for image, similarity in sorted_similarities[:5]:
            print("Similarity:", similarity, "- Image:", image)
    except KeyError as e:
        print('Error: Image not found -', e)
    except Exception as e:
        print('Error:', e)
def search_online():
    image_rel_path = input("Enter the relative path of the image to search:\n")
    with open(image_rel_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    conn = http.client.HTTPConnection("beard-app.herokuapp.com")
    payload = encoded_string.decode('utf-8')
    headers = {'Content-Type': "text/plain"}
    conn.request("PUT", "image_clustering", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
if __name__ == '__main__':
    search_online()