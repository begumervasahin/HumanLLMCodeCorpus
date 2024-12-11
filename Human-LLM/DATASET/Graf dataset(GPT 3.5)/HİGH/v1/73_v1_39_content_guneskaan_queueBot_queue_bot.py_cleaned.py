from collections import deque
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
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
    def fonk1(self, b2, b3, b13):
        self.b2 = b2
        self.b3 = b3
        self.b4 = "queueBot"
        self.b5 = ":robot_face:"
        self.b6 = ""
        self.b7 = deque()
        self.b8 = WebClient(token=b13)
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
        b9 = [self.fonk4(user) for user in self.b7]
        if not b9:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
                }
            }
        b9.insert(0, {
            "type": "mrkdwn",
            "text": ":one: : "
        })
        return {
            "type": "context",
            "b9": b9
        }
    def fonk4(self, user):
        b10 = self.fonk5(user["id"])
        return {
            "type": "image",
            "b10": b10,
            "alt_text": user["b3"]
        }
    def fonk5(self, user_id):
        return ""
    def fonk6(self, user):
        if user in self.b7:
            logging.info('Error: User is already in the queue.')
            return
        self.b7.append(user)
    def fonk7(self):
        try:
            b11 = self.b8.chat_postMessage(**self.fonk2())
            self.b6 = b11["ts"]
        except SlackApiError as e:
            logging.error(f"Error posting message: {e.b11['error']}")
if b12 = = "__main__":
    b2 = "your_channel_id"
    b3 = "Your Queue Bot"
    b13 = "your_slack_token"
    b14 = class1(b2, b3, b13)
    b15 = {"id": "user_id_1", "b3": "User 1"}
    b16 = {"id": "user_id_2", "b3": "User 2"}
    b14.fonk6(b15)
    b14.fonk6(b16)
    b14.fonk7()