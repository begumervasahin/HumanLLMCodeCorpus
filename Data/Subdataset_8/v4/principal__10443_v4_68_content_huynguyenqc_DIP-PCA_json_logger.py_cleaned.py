import json
import logging
def _dict_to_embedded_json(dict_data: dict) -> str:
    return json.dumps(dict_data)[1: -1]
def _convert_log_method(log_method):
    def _inner_convert_log_method(level, msg, args, exc_info=None, extra=None, stack_info=False):
        if isinstance(msg, dict):
            json_msg = _dict_to_embedded_json(msg)
        elif isinstance(msg, str):
            json_msg = _dict_to_embedded_json({'msg': msg})
        else:
            json_msg = _dict_to_embedded_json({'msg': str(msg)})
        return log_method(level, json_msg, args, exc_info, extra, stack_info)
    return _inner_convert_log_method
class JsonLogger(logging.Logger):
    def __getattribute__(self, item):
        if item == '_log':
            return _convert_log_method(super(JsonLogger, self).__getattribute__(item))
        else:
            return super(JsonLogger, self).__getattribute__(item)