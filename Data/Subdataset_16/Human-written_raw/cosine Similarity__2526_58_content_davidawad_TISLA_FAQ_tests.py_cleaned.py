from app import *
from constants import *
def fonk1(text, b1 = None, buttons=None):
    b2 = {}
    b2['text'] = text
    b2['b1'] = b1
    b2['buttons'] = buttons
    return b2
class class1(object):
    def fonk2(self):
        b3 = bot_response("Hello")
        b4 = fonk1("Hello! Iâm Sloan, your automated guide for advice on your student loans brought to you by TISLA. This is not legal advice but simple guidance to help you manage your student loan debt. Send 'restart' at any time to restart. Ready? Simply type your question and Iâll try and guide you to the best way to manage your student debt!", raw_response_data['replies']['intro'])
        assert b3.get('text', None) == b4.get('text')
        assert b3.get('buttons', None) == b4.get('buttons')
        assert b3.get('b1', None) == b4.get('b1')