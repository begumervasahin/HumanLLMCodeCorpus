import os
import csv
import base64
import http.client
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
image_vectors = {}
def read_image_vectors_from_csv():
    for filename in os.listdir('./csv'):
        with open(os.path.join('./csv', filename), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                image_vectors[row[1]] = np.fromstring(row[2][1:-1], dtype=np.float_, sep=' ')
def add_image_to_dictionary(image_rel_path):
    img2vec = Img2Vec()
    filename = os.fsdecode(image_rel_path)
    print("Processing image: %s" % filename)
    img = Image.open(os.path.join('.', filename))
    vec = img2vec.get_vec(img)
    image_vectors[filename] = vec
def search_for_similar_images_offline():
    image_rel_path = str(input("Enter the relative path of the image to search?\n"))
    add_image_to_dictionary(image_rel_path)
    read_image_vectors_from_csv()
    try:
        similarities = {}
        for key in list(image_vectors.keys()):
            if key == image_rel_path:
                continue
            similarities[key] = cosine_similarity(image_vectors[image_rel_path].reshape((1, -1)),
                                                   image_vectors[key].reshape((1, -1)))[0][0]
        sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        for k, v in sorted_similarities[:5]:
            print(v, k)
    except KeyError as e:
        print('Could not find filename %s' % e)
    except Exception as e:
        print(e)
def search_for_similar_images_online():
    image_rel_path = str(input("Enter the relative path of the image to search?\n"))
    with open(image_rel_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    conn = http.client.HTTPConnection("beard-app.herokuapp.com")
    payload = encoded_string.decode('utf-8')
    headers = {
        'Content-Type': "text/plain"
    }
    conn.request("PUT", "image_clustering", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
if __name__ == '__main__':
    search_for_similar_images_online()