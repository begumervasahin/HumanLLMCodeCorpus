from jinja2 import Environment, FileSystemLoader
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
    return '\n'.join(fonk1(b3, group_size) for _ in range(b5))
class class1(object):
    @cherrypy.expose
    def fonk3(self):
        b6 = [fonk2() for _ in range(a4)]
        b7 = b8.get_template('one_time_pad')
        return b7.render(b6 = b6)
b8 = Environment(loader=FileSystemLoader('.'))
b8.filters['enumerate'] = enumerate
if b9 = = '__main__':
    cherrypy.quickstart(class1(), '/', b10 = b1)