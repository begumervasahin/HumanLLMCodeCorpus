import logging
from collections import deque
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
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
    def __init__(self, channel, name, slack_token):
        self.channel = channel
        self.name = name
        self.username = "queueBot"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
        self.queue = deque()
        self.slack_client = WebClient(token=slack_token)
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
            return self._get_empty_queue_block()
        else:
            return self._get_filled_queue_block()
    def _get_empty_queue_block(self):
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "There is no one in this queue yet! Click the \"Line Up\" button to be the first in the line!"
            }
        }
    def _get_filled_queue_block(self):
        elements = [{"type": "mrkdwn", "text": f":{i + 1}: {user['name']}"} for i, user in enumerate(self.queue)]
        return {"type": "context", "elements": elements}
    def insert_queue(self, user):
        if user in self.queue:
            logging.info('Error: User is already in the queue.')
        else:
            self.queue.append(user)
    def send_message(self):
        try:
            response = self.slack_client.chat_postMessage(**self.get_message_payload())
            self.timestamp = response["ts"]
        except SlackApiError as e:
            logging.error(f"Error posting message: {e.response['error']}")
if __name__ == "__main__":
    channel = "your_channel_id"
    name = "Your Queue Bot"
    slack_token = "your_slack_token"
    queue_bot = QueueBot(channel, name, slack_token)
    user1 = {"id": "user_id_1", "name": "User 1"}
    user2 = {"id": "user_id_2", "name": "User 2"}
    queue_bot.insert_queue(user1)
    queue_bot.insert_queue(user2)
    queue_bot.send_message()