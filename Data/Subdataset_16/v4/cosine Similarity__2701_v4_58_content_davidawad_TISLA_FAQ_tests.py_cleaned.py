from app import bot_response
from constants import raw_response_data
def fonk1(text, b1 = None, buttons=None):
    return {
        'text': text,
        'b1': b1,
        'buttons': buttons
    }
class class1:
    def fonk2(self):
        b2 = bot_response("Hello")
        b3 = (
            "Hello! Im Sloan, your automated guide for advice on your student loans brought to you by TISLA. "
            "This is not legal advice but simple guidance to help you manage your student loan debt. "
            "Send 'restart' at any time to restart. Ready? Simply type your question and Ill try and guide you "
            "to the best way to manage your student debt!"
        )
        b4 = fonk1(
            b3,
            b1 = raw_response_data['replies']['intro']
        )
        assert b2.get('text') == b4.get('text')
        assert b2.get('buttons') == b4.get('buttons')
        assert b2.get('b1') == b4.get('b1')
if b5 = = "__main__":
    b6 = class1()
    b6.fonk2()
    print("Test passed.")