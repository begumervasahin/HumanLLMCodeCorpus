from flask import Flask, render_template, request
import socket
import time
app = Flask(__name__)
app.secret_key = "Non-seen"
COMMON_PORTS = [21, 22, 23, 25, 27, 50, 53, 69, 70, 80, 87, 88, 109, 110, 113, 143, 1080, 8080, 8088]
@app.route('/', methods=['GET', 'POST'])
def scan():
    if request.method == 'GET':
        return render_template("scaner.html")
    area = request.form['area'].lower()
    ip = request.form['url']
    try:
        if area == 'ip':
            return handle_ip(ip)
        elif area == 'name':
            return handle_name(ip)
        elif area == 'ports':
            return handle_ports(ip)
        elif area == 'services':
            return handle_services(ip)
        else:
            return render_template('scaner.html', error=True)
    except Exception as e:
        return f"An error occurred:<hr>{e}"
def handle_ip(ip):
    address = socket.getfqdn(ip) if ip[0].isdigit() else socket.gethostbyname(ip)
    return render_template('scaner.html', addr='IP', loc=ip, res=address)
def handle_name(ip):
    address = socket.getfqdn(ip)
    return render_template('scaner.html', addr='Name', loc=ip, res=address)
def handle_ports(ip):
    open_ports = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in COMMON_PORTS:
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            time.sleep(0.001)
    if not open_ports:
        open_ports = [0]
    return render_template('scaner.html', hosts=open_ports)
def handle_services(ip):
    services = {}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        for port in COMMON_PORTS:
            result = sock.connect_ex((ip, port))
            service = get_service_name(port)
            status = "running" if result == 0 else "not running"
            services[port] = [service, status]
    return render_template('scaner.html', services=services)
def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "unknown"
if __name__ == '__main__':
    app.run(debug=True)