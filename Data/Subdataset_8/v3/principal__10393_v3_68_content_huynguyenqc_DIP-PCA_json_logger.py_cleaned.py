import json
import logging
def format_dict_to_json(dict_data: dict) -> str:
    return json.dumps(dict_data)[1: -1]
def wrap_logging_method(log_method):
    def convert_log_method(level, msg, args, exc_info=None, extra=None, stack_info=False):
        if isinstance(msg, dict):
            json_msg = format_dict_to_json(msg)
        elif isinstance(msg, str):
            json_msg = format_dict_to_json({'msg': msg})
        else:
            json_msg = format_dict_to_json({'msg': str(msg)})
        return log_method(level, json_msg, args, exc_info, extra, stack_info)
    return convert_log_method
class JsonLogger(logging.Logger):
    def __getattribute__(self, item):
        if item == '_log':
            return wrap_logging_method(super(JsonLogger, self).__getattribute__(item))
        else:
            return super(JsonLogger, self).__getattribute__(item)
if __name__ == "__main__":
    logging.setLoggerClass(JsonLogger)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.info({"key": "value"})
    logger.warning("This is a warning message")
    try:
        result = 1 / 0
    except Exception as e:
        logger.error("An error occurred", exc_info=True)