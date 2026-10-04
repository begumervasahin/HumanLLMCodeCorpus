from app import *
from constants import *
def return_response_object(text, quick_replies=None, buttons=None):
    ret_obj = {}
    ret_obj['text'] = text
    ret_obj['quick_replies'] = quick_replies
    ret_obj['buttons'] = buttons
    return ret_obj
class TestBotResponses(object):
    def test_intro_message_response(self):
        reply = bot_response("Hello")
        response_obj = return_response_object("Hello! Iâm Sloan, your automated guide for advice on your student loans brought to you by TISLA. This is not legal advice but simple guidance to help you manage your student loan debt. Send 'restart' at any time to restart. Ready? Simply type your question and Iâll try and guide you to the best way to manage your student debt!", raw_response_data['replies']['intro'])
        assert reply.get('text', None) == response_obj.get('text')
        assert reply.get('buttons', None) == response_obj.get('buttons')
        assert reply.get('quick_replies', None) == response_obj.get('quick_replies')