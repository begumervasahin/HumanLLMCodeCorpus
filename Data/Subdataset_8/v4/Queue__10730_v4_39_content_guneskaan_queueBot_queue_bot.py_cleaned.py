from queue import Queue
from collections import deque
import logging
import slack
from client_helpers import fetch_image_url_for_user_id
logging.getLogger().setLevel(logging.INFO)
class QueueBot:
    LINE_BLOCK = {
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
    def __init__(self, channel, name):
        self.channel = channel
        self.name = name
        self.username = "queueBot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.Q = deque()
    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.LINE_BLOCK,
                self._get_queue_block()
            ],
        }
    def _get_queue_block(self):
        elements = [user_to_block_kit_element(user) for user in self.Q]
        if not elements:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
                }
            }
        elements = [{"type": "mrkdwn", "text": f":{i + 1}: : "} for i in range(len(elements))] + elements
        return {
            "type": "context",
            "elements": elements
        }
    def insert_queue(self, user):
        if user in self.Q:
            logging.info('Error: User is already in the queue.')
            return
        self.Q.append(user)
def user_to_block_kit_element(user):
    image_url = fetch_image_url_for_user_id(user["id"])
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": user["name"]
    }