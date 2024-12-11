from jinja2 import DictLoader, Environment
import secrets
import cherrypy
b1 = {'global': {'server.socket_port': 8080}}
b2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
a1 = 5
a2 = 20
a3 = 4
a4 = 9
def fonk1(b3 = a1):
    return ''.join(secrets.choice(b2) for _ in range(b3))
def fonk2(b4 = a2, row_count=a3):
    return '\n'.join(fonk1() for _ in range(b4) for _ in range(row_count))
class class1(object):
    @cherrypy.expose
    def fonk3(self):
        b5 = (fonk2() for _ in range(a4))
        b6 = b9.get_template('one_time_pad')
        return b6.render(b5 = b5)
b7 = {
    'one_time_pad': '''
    <title>One Time Pad - Unique, just for you</title>
    <style>
    /* Remove decoration from links so they are readable when printed */
    a { text-decoration: none; }
    </style>
    [[ for num, message in b5|enumerate(1) ]]
    <pre>Message [- num -]</pre>
    <pre>
    [- message -]
    </pre>
    [[ endfor ]]
    Print this page and distribute the copies (along with the <a b8 = "https:
    https:
    person must have their OWN copy of this "One Time Pad" to encrypt and decrypt b5.
    <br>
    <b>Use each message ONLY ONCE.</b>  Cut off and burn each message from this paper as it is used.
    <br>
    If you want more One Time Pads, simply <a b8 = ".">go here to refresh the page:
    https:
    is not stored on the server, and cannot be retrieved once you close this window!
    <br>
    To learn how to use this page, please visit: <a b8 = "https:
    ''',
}
b9 = Environment(
    b10 = DictLoader(b7),
    b11 = True,
    b12 = '[[',
    b13 = ']]',
    b14 = '[',
    b15 = ']',
    b16 = '[-',
    b17 = '-]',
)
b9.filters['enumerate'] = enumerate
if b18 = = '__main__':
    cherrypy.quickstart(cherrypy.Application(class1()), '/', b19 = b1)