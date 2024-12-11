import requests
import sys
import b8
import time
import os
from gtts import gTTS
import numpy as np
class class1:
    def fonk1(self, b12, b4, b11, b1 = 8080):
        self.b2 = ""
        self.b3 = b12
        self.b4 = b4
        self.b5 = f"{b11}:{b1}"
        self.b6 = np.random.randint(10000)
    def fonk2(self):
        self.fonk3(f"Beginning journey from {self.b3} to {self.b4}")
        while True:
            b7 = b8.loads(requests.post(self.b5,
                                                b8 = {"prev": self.b2,
                                                      "curr": self.b3,
                                                      "dest": self.b4}).text)
            if b7["status"] == -1:
                self.fonk3("You cannot reach your b4 from the given starting point")
                break
            elif b7["status"] == 1:
                self.fonk3("You have arrived at your b4")
                break
            else:
                self.fonk3(f"Turn onto {b7['road']}")
                self.fonk3(f"Current expected remaining time to {self.b4}: {b7['total_wait']} seconds")
                self.b2 = self.b3
                self.b3 = b7['next']
                time.sleep(b7['wait'])
    def fonk3(self, message):
        b9 = gTTS(text=message, lang='en')
        b9.save(f"speech.{self.b6}.mp3")
        print(message)
        os.system(f"ffplay -nodisp -autoexit -volume 100 -loglevel quiet speech.{self.b6}.mp3")
def fonk4(argv):
    b10 = len(argv)
    b12, b4, b11 = "", "", ""
    if b10 = = 4:
        b12 = argv[1]
        b4 = argv[2]
        b11 = argv[3]
    b13 = class1(b12, b4, b11)
    b13.fonk2()
if b14 = = "__main__":
    fonk4(sys.argv)