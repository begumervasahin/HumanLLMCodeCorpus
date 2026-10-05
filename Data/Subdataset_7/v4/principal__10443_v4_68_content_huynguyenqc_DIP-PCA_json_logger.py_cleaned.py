import json
import logging
def fonk1(dict_data: dict) -> str:
    return json.dumps(dict_data)[1: -1]
def fonk2(log_method):
    def fonk3(level, msg, args, b1 = None, extra=None, stack_info=False):
        if isinstance(msg, dict):
            b2 = fonk1(msg)
        elif isinstance(msg, str):
            b2 = fonk1({'msg': msg})
        else:
            b2 = fonk1({'msg': str(msg)})
        return log_method(level, b2, args, b1, extra, stack_info)
    return _inner_convert_log_method
class class1(logging.Logger):
    def fonk4(self, b3):
        if b3 = = '_log':
            return fonk2(super(class1, self).fonk4(b3))
        else:
            return super(class1, self).fonk4(b3)