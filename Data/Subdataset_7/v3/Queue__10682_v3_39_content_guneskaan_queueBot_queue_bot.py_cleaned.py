import logging
from collections import deque
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
    def fonk1(self, b2, b3, b12):
        self.b2 = b2
        self.b3 = b3
        self.b4 = "queueBot"
        self.b5 = ":robot_face:"
        self.b6 = ""
        self.b7 = deque()
        self.b8 = WebClient(token=b12)
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
        if not self.b7:
            return self.fonk4()
        else:
            return self.fonk5()
    def fonk4(self):
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "There is no one in this b7 yet! Click the \"Line Up\" button to be the first in the line!"
            }
        }
    def fonk5(self):
        b9 = [{"type": "mrkdwn", "text": f":{i + 1}: {user['b3']}"} for i, user in enumerate(self.b7)]
        return {"type": "context", "b9": b9}
    def fonk6(self, user):
        if user in self.b7:
            logging.info('Error: User is already in the b7.')
        else:
            self.b7.append(user)
    def fonk7(self):
        try:
            b10 = self.b8.chat_postMessage(**self.fonk2())
            self.b6 = b10["ts"]
        except SlackApiError as e:
            logging.error(f"Error posting message: {e.b10['error']}")
if b11 = = "__main__":
    b2 = "your_channel_id"
    b3 = "Your Queue Bot"
    b12 = "your_slack_token"
    b13 = class1(b2, b3, b12)
    b14 = {"id": "user_id_1", "b3": "User 1"}
    b15 = {"id": "user_id_2", "b3": "User 2"}
    b13.fonk6(b14)
    b13.fonk6(b15)
    b13.fonk7()