import requests
import sys
import json
import time
import os
from gtts import gTTS
import numpy as np
class Car:
    def __init__(self, current_location, destination, server_url, port=8080):
        self.previous_location = ""
        self.current_location = current_location
        self.destination = destination
        self.api_url = f"{server_url}:{port}"
        self.car_id = np.random.randint(10000)
    def journey_loop(self):
        self.print_and_say(f"Beginning journey from {self.current_location} to {self.destination}")
        while True:
            response = self.make_api_request()
            if response["status"] == -1:
                self.print_and_say("Unable to reach the destination from the current location")
                break
            elif response["status"] == 1:
                self.print_and_say("Arrived at the destination")
                break
            else:
                self.print_and_say(f"Turn onto {response['road']}")
                self.print_and_say(f"Estimated time to {self.destination}: {response['total_wait']} seconds")
                self.update_location(response)
    def make_api_request(self):
        payload = {"prev": self.previous_location, "curr": self.current_location, "dest": self.destination}
        response = requests.post(self.api_url, json=payload).text
        return json.loads(response)
    def update_location(self, response):
        self.previous_location = self.current_location
        self.current_location = response['next']
        time.sleep(response['wait'])
    def print_and_say(self, message):
        text_to_speech = gTTS(text=message, lang='en')
        audio_file = f"speech.{self.car_id}.mp3"
        text_to_speech.save(audio_file)
        print(message)
        os.system(f"ffplay -nodisp -autoexit -volume 100 -loglevel quiet {audio_file}")
def initialize_car(argv):
    if len(argv) == 4:
        current_location, destination, server_url = argv[1:]
        car = Car(current_location, destination, server_url)
        car.journey_loop()
    else:
        print("Usage: python car_navigation.py <current_location> <destination> <server_url>")
if __name__ == "__main__":
    initialize_car(sys.argv)