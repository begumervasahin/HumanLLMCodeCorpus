import os
import csv
import base64
from PIL import Image
import numpy as np
import http.client
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
class ImageSearch:
    def __init__(self):
        self.pics = {}
    def read_from_csv(self, csv_dir='./csv'):
        for filename in os.listdir(csv_dir):
            filepath = os.path.join(csv_dir, filename)
            with open(filepath, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    image_name = row[1]
                    vector_str = row[2][1:-1]
                    self.pics[image_name] = np.fromstring(vector_str, dtype=np.float_, sep=' ')
    def add_to_dict(self, pic_rel_path):
        img2vec = Img2Vec()
        img_path = os.path.join('.', pic_rel_path)
        img = Image.open(img_path)
        vec = img2vec.get_vec(img)
        self.pics[pic_rel_path] = vec
    def search_offline(self, pic_rel_path):
        self.add_to_dict(pic_rel_path)
        self.read_from_csv()
        try:
            similarities = self.compute_similarities(pic_rel_path)
            sorted_similarities = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
            print("Top 5 similar images:")
            for similarity, image_name in sorted_similarities[:5]:
                print(f"{similarity:.4f} - {image_name}")
        except KeyError as e:
            print(f'Could not find filename: {e}')
        except Exception as e:
            print(e)
    def compute_similarities(self, pic_rel_path):
        similarities = {}
        target_vector = self.pics[pic_rel_path].reshape((1, -1))
        for image_name, vector in self.pics.items():
            if image_name != pic_rel_path:
                similarity = cosine_similarity(target_vector, vector.reshape((1, -1)))[0][0]
                similarities[image_name] = similarity
        return similarities
    def search_online(self, pic_rel_path):
        with open(pic_rel_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        conn = http.client.HTTPConnection("beard-app.herokuapp.com")
        headers = {'Content-Type': "text/plain"}
        conn.request("PUT", "/image_clustering", encoded_string, headers)
        response = conn.getresponse()
        data = response.read()
        print(data.decode("utf-8"))
def main():
    img_search = ImageSearch()
    choice = input("Do you want to search online or offline? (online/offline)\n").strip().lower()
    if choice in ['offline', 'online']:
        pic_rel_path = input("Enter relative path of the image to search:\n").strip()
        if choice == 'offline':
            img_search.search_offline(pic_rel_path)
        else:
            img_search.search_online(pic_rel_path)
    else:
        print("Invalid choice. Please enter 'online' or 'offline'.")
if __name__ == '__main__':
    main()