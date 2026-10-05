import requests
import sys
import json
import os
import zipfile
workshopdir = sys.argv[1] if len(sys.argv) >= 3 else sys.exit()
links = sys.argv[2] if len(sys.argv) >= 3 else sys.exit()
mode = True if "install" == (sys.argv[3] if len(sys.argv) >= 3 else sys.exit()) else False
def create_folder(dirs):
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
        return dirs
    else:
        return False
def extract_zip(filename, edir):
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(edir)
    zip_ref.close()
class PluginContent:
    def __init__(self, data):
        self.data = data
        self.fid = data["publishedfileid"]
        self.filename = data["filename"]
        self.file_size = data["file_size"]
        self.file_url = data["file_url"]
        self.file_title = data["title"]
        self.nfilename = "%s-%s.zip" % (self.fid, self.file_title)
        self.fmid = "M%s-%s" % (self.fid, self.file_title)
        self.mfolder = os.path.join(workshopdir, self.fmid)
    def create_folder(self):
        return create_folder(self.mfolder)
    def install(self):
        if self.create_folder():
            local_filename = os.path.join(self.mfolder, self.nfilename)
            r = requests.get(self.file_url, stream=True)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            extract_zip(local_filename, self.mfolder)
            os.remove(local_filename)
            return local_filename
        else:
            return None
    def download(self):
        if self.create_folder():
            local_filename = os.path.join(self.mfolder, self.filename)
            r = requests.get(self.file_url, stream=True)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return local_filename
        else:
            return None
def get_plugin_content(id):
    m = {'itemcount': 1, 'publishedfileids[0]': id}
    r = requests.post("https:
    return PluginContent(json.loads(r.text)["response"]["publishedfiledetails"][0])
def get_pid(url):
    args = [tuple(i.split("=")) for i in url.split("?")[-1].split("&")]
    for name, value in args:
        if name == "id":
            return int(value)
    return None
def main():
    plugins = [i for i in open(links, "r").readlines() if i != ""]
    for plugin in plugins:
        pd = get_pid(plugin)
        if pd:
            d = get_plugin_content(pd)
            if mode:
                if d.install():
                    print(f"{d.fmid} install complete.")
                else:
                    print(f"{d.fmid} already installed.")
            else:
                if d.download():
                    print(f"{d.fmid} download complete.")
                else:
                    print(f"{d.fmid} already downloaded.")
if __name__ == '__main__':
    main()