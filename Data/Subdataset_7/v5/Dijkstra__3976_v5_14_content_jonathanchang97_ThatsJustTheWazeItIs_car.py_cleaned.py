import requests
import sys
import json
import time
import os
from gtts import gTTS
import numpy as np
class class1:
    def fonk1(self, b3, b4, b11, b1 = 8080):
        self.b2 = ""
        self.b3 = b3
        self.b4 = b4
        self.b5 = f"{b11}:{b1}"
        self.b6 = np.random.randint(10000)
    def fonk2(self):
        self.fonk5(f"Beginning journey from {self.b3} to {self.b4}")
        while True:
            b7 = self.fonk3()
            if b7["status"] == -1:
                self.fonk5("Unable to reach the b4 from the current location")
                break
            elif b7["status"] == 1:
                self.fonk5("Arrived at the b4")
                break
            else:
                self.fonk5(f"Turn onto {b7['road']}")
                self.fonk5(f"Estimated time to {self.b4}: {b7['total_wait']} seconds")
                self.fonk4(b7)
    def fonk3(self):
        b8 = {"prev": self.b2, "curr": self.b3, "dest": self.b4}
        b7 = requests.post(self.b5, json=b8).text
        return json.loads(b7)
    def fonk4(self, b7):
        self.b2 = self.b3
        self.b3 = b7['next']
        time.sleep(b7['wait'])
    def fonk5(self, message):
        b9 = gTTS(text=message, lang='en')
        b10 = f"speech.{self.b6}.mp3"
        b9.save(b10)
        print(message)
        os.system(f"ffplay -nodisp -autoexit -volume 100 -loglevel quiet {b10}")
def fonk6(argv):
    if len(argv) == 4:
        b3, b4, b11 = argv[1:]
        b12 = class1(b3, b4, b11)
        b12.fonk2()
    else:
        print("Usage: python car_navigation.py <b3> <b4> <b11>")
if b13 = = "__main__":
    fonk6(sys.argv)