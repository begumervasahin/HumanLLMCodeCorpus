from queue import Queue
from collections import deque
import logging
import slack
from client_helpers import fetch_image_url_for_user_id
logging.getLogger().setLevel(logging.INFO)
class class1:
    b1 = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to queueBot! :wave: \n\n"
                "*Here are the people in the line:*"
            ),
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Line Up"
            },
            "action_id": "action_id",
            "value": "view_alternate_2"
        }
    }
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
        self.b4 = "queueBot"
        self.b5 = ":robot_face:"
        self.b6 = ""
        self.b7 = deque()
    def fonk2(self):
        return {
            "ts": self.b6,
            "b2": self.b2,
            "b4": self.b4,
            "b5": self.b5,
            "blocks": [
                self.b1,
                self.fonk3()
            ],
        }
    def fonk3(self):
        b8 = [fonk5(user) for user in self.b7]
        if not b8:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
                }
            }
        b8 = [{"type": "mrkdwn", "text": f":{i + 1}: : "} for i in range(len(b8))] + b8
        return {
            "type": "context",
            "b8": b8
        }
    def fonk4(self, user):
        if user in self.b7:
            logging.info('Error: User is already in the queue.')
            return
        self.b7.append(user)
def fonk5(user):
    b9 = fetch_image_url_for_user_id(user["id"])
    return {
        "type": "image",
        "b9": b9,
        "alt_text": user["b3"]
    }