import json
import logging
def fonk1(log_method):
    def fonk2(dict_data: dict) -> str:
        return json.dumps(dict_data)[1: -1]
    def fonk3(level, msg, args, b1 = None, extra=None, stack_info=False):
        if isinstance(msg, dict):
            b2 = fonk2(msg)
            return log_method(level, b2, args, b1, extra, stack_info)
        elif isinstance(msg, str):
            b2 = fonk2({'msg': msg})
            return log_method(level, b2, args, b1, extra, stack_info)
        else:
            b2 = fonk2({'msg': str(msg)})
            return log_method(level, b2, args, b1, extra, stack_info)
    return _convert_log_method
class class1(logging.Logger):
    def fonk4(self, b3):
        if b3 = = '_log':
            return fonk1(super(class1, self).fonk4(b3))
        else:
            return super(class1, self).fonk4(b3)