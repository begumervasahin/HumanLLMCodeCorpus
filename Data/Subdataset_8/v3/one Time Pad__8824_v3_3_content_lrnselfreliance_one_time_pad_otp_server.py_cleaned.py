import secrets
import cherrypy
from jinja2 import Environment, FileSystemLoader
CONFIG = {'global': {'server.socket_port': 8080}}
OTP_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
GROUP_SIZE = 5
GROUP_COUNT = 20
ROW_COUNT = 4
MESSAGE_COUNT = 9
def generate_row(group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    groups = [''.join([secrets.choice(OTP_CHARS) for _ in range(group_size)]) for _ in range(group_count)]
    return ' '.join(groups)
def generate_message(row_count=ROW_COUNT, group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    return '\n'.join(generate_row(group_count, group_size) for _ in range(row_count))
class Root(object):
    @cherrypy.expose
    def one_time_pad(self):
        messages = [generate_message() for _ in range(MESSAGE_COUNT)]
        template = env.get_template('one_time_pad')
        return template.render(messages=messages)
env = Environment(loader=FileSystemLoader('.'))
env.filters['enumerate'] = enumerate
if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/', config=CONFIG)