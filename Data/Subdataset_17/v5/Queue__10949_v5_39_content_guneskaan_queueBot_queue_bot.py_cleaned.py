import logging
from collections import deque
from queue import Queue
import slack
from client_helpers import fetchImageUrlForUserId
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
            "action_id": "line_up",
            "value": "view_queue"
        }
    }
    def __init__(self, channel, name):
        self.channel = channel
        self.name = name
        self.username = "queueBot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.queue = deque()
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
        if not self.queue:
            return {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": 'There is no one in this queue yet! Click the "Line Up" button to be the first in the line!'
                }
            }
        elements = [self._user_to_block_kit_element(user) for user in self.queue]
        elements.insert(0, {"type": "mrkdwn", "text": ":one: : "})
        return {
            "type": "context",
            "elements": elements
        }
    def insert_queue(self, user):
        if user in self.queue:
            logging.info('Error: User is already in the queue.')
            return
        self.queue.append(user)
    @staticmethod
    def _user_to_block_kit_element(user):
        image_url = fetchImageUrlForUserId(user["id"])
        return {
            "type": "image",
            "image_url": image_url,
            "alt_text": user["name"]
        }