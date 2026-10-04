import logging
from collections import deque
from queue import Queue
import slack
from client_helpers import fetchImageUrlForUserId
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
        b8 = list(map(user_to_block_kit_element, self.b7))
        if not b8:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
                }
            }
        b8.insert(0, {
            "type": "mrkdwn",
            "text": ":one: : "
        })
        return {
            "type": "context",
            "b8": b8
        }
    def fonk4(self, user):
        if user in self.b7:
            logging.info('Error: User is already in the queue.')
            return
        self.b7.append(user)
        logging.info(f'User {user["b3"]} added to the queue.')
def fonk5(user):
    b9 = fetchImageUrlForUserId(user["id"])
    return {
        "type": "image",
        "b9": b9,
        "alt_text": user["b3"]
    }
if b10 = = "__main__":
    b11 = class1(b2="your-b2-id", b3="class1")
    b12 = {"id": "U12345", "b3": "Alice"}
    b13 = {"id": "U67890", "b3": "Bob"}
    b11.fonk4(b12)
    b11.fonk4(b13)
    b14 = b11.fonk2()
    print(b14)