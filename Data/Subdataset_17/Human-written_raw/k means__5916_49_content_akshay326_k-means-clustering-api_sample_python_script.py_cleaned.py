from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
import numpy as np
import http.client
import os
import csv
import base64
pics = {}
def read_from_csv():
    for filename in os.listdir('./csv'):
        with open('./csv/'+filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                pics[row[1]] = np.fromstring(row[2][1:-1], dtype=np.float_, sep=' ')
def add_to_dict(pic_rel_path):
    img2vec = Img2Vec()
    filename = os.fsdecode(pic_rel_path)
    print("Filename is: %s" % filename)
    img = Image.open(os.path.join('.', filename))
    vec = img2vec.get_vec(img)
    pics[filename] = vec
def search_offline():
    pic_rel_path = str(input("Enter relative path of the image to search?\n"))
    add_to_dict(pic_rel_path)
    read_from_csv()
    try:
        sims = {}
        for key in list(pics.keys()):
            if key == pic_rel_path:
                continue
            sims[key] = cosine_similarity(pics[pic_rel_path].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]
        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)
        for v, k in d_view[0:5]:
            print(v, k)
    except KeyError as e:
        print('Could not find filename %s' % e)
    except Exception as e:
        print(e)
def search_online():
    pic_rel_path = str(input("Enter relative path of the image to search?\n"))
    with open(pic_rel_path, "rb") as image_file:
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
    search_online()