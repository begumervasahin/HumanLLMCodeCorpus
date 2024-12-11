import requests
import sys
import json
import time
import os
from gtts import gTTS
import numpy as np
class class1:
    def fonk1(self, b3, b4, b10, b1 = 8080):
        self.b2 = ""
        self.b3 = b3
        self.b4 = b4
        self.b5 = f"{b10}:{b1}"
        self.b6 = np.random.randint(10000)
    def fonk2(self):
        self.fonk5(f"Beginning journey from {self.b3} to {self.b4}")
        while True:
            b7 = self.fonk3({"prev": self.b2,
                                          "curr": self.b3,
                                          "dest": self.b4})
            if b7["status"] == -1:
                self.fonk5("You cannot reach your b4 from the given starting point")
                break
            elif b7["status"] == 1:
                self.fonk5("You have arrived at your b4")
                break
            else:
                self.fonk5(f"Turn onto {b7['road']}")
                self.fonk5(f"Current expected remaining time to {self.b4}: {b7['total_wait']} seconds")
                self.fonk4(b7)
    def fonk3(self, payload):
        b7 = requests.post(self.b5, json=payload).text
        return json.loads(b7)
    def fonk4(self, b7):
        self.b2 = self.b3
        self.b3 = b7['next']
        time.sleep(b7['wait'])
    def fonk5(self, message):
        b8 = gTTS(text=message, lang='en')
        b9 = f"speech.{self.b6}.mp3"
        b8.save(b9)
        print(message)
        os.system(f"ffplay -nodisp -autoexit -volume 100 -loglevel quiet {b9}")
def fonk6(argv):
    if len(argv) == 4:
        curr_location, b4, b10 = argv[1:]
        b11 = class1(curr_location, b4, b10)
        b11.fonk2()
    else:
        print("Usage: python car_navigation.py <b3> <b4> <b10>")
if b12 = = "__main__":
    fonk6(sys.argv)