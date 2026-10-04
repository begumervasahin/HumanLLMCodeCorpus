import requests
import sys
import json
import os
import zipfile
def fonk1():
    if len(sys.argv) < 4:
        sys.exit("Usage: script.py <b2> <links_file> <install|download>")
    return sys.argv[1], sys.argv[2], sys.argv[3].lower() == "install"
def fonk2(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return directory
    return None
def fonk3(b4, extract_dir):
    with zipfile.ZipFile(b4, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    os.remove(b4)
class class1:
    def fonk4(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1["publishedfileid"]
        self.b4 = b1["b4"]
        self.b5 = b1["b5"]
        self.b6 = b1["title"]
        self.b7 = f"{self.b3}-{self.b6}.zip"
        self.b8 = f"M{self.b3}-{self.b6}"
        self.b9 = os.path.join(b2, self.b8)
    def fonk5(self):
        return fonk5(self.b9)
    def fonk6(self):
        if self.fonk5():
            b10 = os.path.join(self.b9, self.b7)
            b11 = requests.get(self.b5, stream=True)
            with open(b10, 'wb') as f:
                for chunk in b11.iter_content(b12 = 1024):
                    if chunk:
                        f.write(chunk)
            fonk3(b10, self.b9)
            return b10
        return None
    def fonk7(self):
        if self.fonk5():
            b10 = os.path.join(self.b9, self.b4)
            b11 = requests.get(self.b5, stream=True)
            with open(b10, 'wb') as f:
                for chunk in b11.iter_content(b12 = 1024):
                    if chunk:
                        f.write(chunk)
            return b10
        return None
def fonk8(b17, b2):
    b13 = {'itemcount': 1, 'publishedfileids[0]': b17}
    b11 = requests.post("https:
    b1 = json.loads(b11.text)["b11"]["publishedfiledetails"][0]
    return class1(b1, b2)
def fonk9(url):
    b14 = dict(tuple(arg.split("=")) for arg in url.split("?")[-1].split("&"))
    return int(b14.get("id", None))
def fonk10():
    b2, links_file, b15 = fonk1()
    with open(links_file, "r") as f:
        b16 = [line.strip() for line in f.readlines() if line.strip()]
    for plugin_url in b16:
        b17 = fonk9(plugin_url)
        if b17:
            b18 = fonk8(b17, b2)
            if b15:
                if b18.fonk6():
                    print(f"{b18.b8} install complete.")
                else:
                    print(f"{b18.b8} already installed.")
            else:
                if b18.fonk7():
                    print(f"{b18.b8} download complete.")
                else:
                    print(f"{b18.b8} already downloaded.")
if b19 = = '__main__':
    fonk10()