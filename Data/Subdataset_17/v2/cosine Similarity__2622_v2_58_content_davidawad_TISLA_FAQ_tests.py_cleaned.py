from app import bot_response
from constants import raw_response_data
def return_response_object(text, quick_replies=None, buttons=None):
    return {
        'text': text,
        'quick_replies': quick_replies,
        'buttons': buttons
    }
class TestBotResponses:
    def test_intro_message_response(self):
        reply = bot_response("Hello")
        expected_text = (
            "Hello! Im Sloan, your automated guide for advice on your student loans brought to you by TISLA. "
            "This is not legal advice but simple guidance to help you manage your student loan debt. "
            "Send 'restart' at any time to restart. Ready? Simply type your question and Ill try and guide you "
            "to the best way to manage your student debt!"
        )
        response_obj = return_response_object(expected_text, quick_replies=raw_response_data['replies']['intro'])
        assert reply.get('text') == response_obj.get('text')
        assert reply.get('buttons') == response_obj.get('buttons')
        assert reply.get('quick_replies') == response_obj.get('quick_replies')
if __name__ == "__main__":
    test_bot_responses = TestBotResponses()
    test_bot_responses.test_intro_message_response()
    print("Test passed.")