
from jinja2 import DictLoader, Environment
import secrets
import cherrypy
b1 = {'global': {'server.socket_port': 8080}}
b2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
a1 = 5
a2 = 20
a3 = 4
a4 = 9
def fonk1(b3 = a2, group_size=a1):
    b4 = []
    for _ in range(b3):
        b4.append(''.join([secrets.choice(b2) for _ in range(group_size)]))
    return ' '.join(b4)
def fonk2(b5 = a3, b3=a2, group_size=a1):
    return '\n'.join(fonk1(b3, group_size) for _ in range(a3))
class class1(object):
    @cherrypy.expose
    def fonk3(self):
        b6 = (fonk2() for _ in range(a4))
        b7 = b10.get_template('one_time_pad')
        return b7.render(b6 = b6)
b8 = {'one_time_pad': '''
<title>One Time Pad - Unique, just for you</title>
<style>
/* Remove decoration from links so they are readable when printed */
a { text-decoration: none; }
</style>
[[ for num, message in b6|enumerate(1) ]]
<pre>Message [- num -]</pre>
<pre>
[- message -]
</pre>
[[ endfor ]]
Print this page and distribute the copies (along with the <a b9 = "https:
https:
person must have their OWN copy of this "One Time Pad" to encrypt and decrypt b6.
<br>
<b>Use each message ONLY ONCE.</b>  Cut off and burn each message from this paper as it is used.
<br>
If you want more One Time Pads, simply <a b9 = ".">go here to refresh the page:
https:
is not stored on the server, and cannot be retrieved once you close this window!
<br>
To learn how to use this page, please visit: <a b9 = "https:
''',
}
b10 = Environment(
    b11 = DictLoader(b8),
    b12 = True,
    b13 = '[[',
    b14 = ']]',
    b15 = '[
    b16 = '
    b17 = '[-',
    b18 = '-]',
)
b10.filters['enumerate'] = enumerate
if b19 = = '__main__':
    cherrypy.quickstart(cherrypy.Application(class1()), '/', b20 = b1)