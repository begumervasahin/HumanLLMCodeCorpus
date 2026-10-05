from jinja2 import DictLoader, Environment
import secrets
import cherrypy
CONFIG = {'global': {'server.socket_port': 8080}}
OTP_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
GROUP_SIZE = 5
GROUP_COUNT = 20
ROW_COUNT = 4
MESSAGE_COUNT = 9
def generate_row(group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    groups = []
    for _ in range(group_count):
        groups.append(''.join([secrets.choice(OTP_CHARS) for _ in range(group_size)]))
    return ' '.join(groups)
def generate_message(row_count=ROW_COUNT, group_count=GROUP_COUNT, group_size=GROUP_SIZE):
    return '\n'.join(generate_row(group_count, group_size) for _ in range(row_count))
class Root(object):
    @cherrypy.expose
    def one_time_pad(self):
        messages = (generate_message() for _ in range(MESSAGE_COUNT))
        template = env.get_template('one_time_pad')
        return template.render(messages=messages)
templates = {
    'one_time_pad': '''
    <title>One Time Pad - Unique, just for you</title>
    <style>
    /* Remove decoration from links so they are readable when printed */
    a { text-decoration: none; }
    </style>
    [[ for num, message in messages|enumerate(1) ]]
    <pre>Message [- num -]</pre>
    <pre>
    [- message -]
    </pre>
    [[ endfor ]]
    Print this page and distribute the copies (along with the <a href="https:
    https:
    person must have their OWN copy of this "One Time Pad" to encrypt and decrypt messages.
    <br>
    <b>Use each message ONLY ONCE.</b>  Cut off and burn each message from this paper as it is used.
    <br>
    If you want more One Time Pads, simply <a href=".">go here to refresh the page:
    https:
    is not stored on the server, and cannot be retrieved once you close this window!
    <br>
    To learn how to use this page, please visit: <a href="https:
    ''',
}
env = Environment(
    loader=DictLoader(templates),
    autoescape=True,
    block_start_string='[[',
    block_end_string=']]',
    comment_start_string='[',
    comment_end_string=']',
    variable_start_string='[-',
    variable_end_string='-]',
)
env.filters['enumerate'] = enumerate
if __name__ == '__main__':
    cherrypy.quickstart(cherrypy.Application(Root()), '/', config=CONFIG)