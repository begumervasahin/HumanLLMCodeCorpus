from flask import Flask, render_template, request
from b9.weighted_graph import weighted_graph
import time
b1 = ['EUR', 'USD', 'JPY', 'CHF', 'AUD', 'CAD', 'NZD', 'GBP', 'SEK', 'NOK', 'MXN', 'TRY', 'ZAR', 'CNH', 'XAU', 'XAG']
b2 = ', '.join(b1)
b3 = Flask(b15)
@b3.route('/', b4 = ['GET', 'POST'])
def fonk1():
    b5 = ""
    b6 = ""
    if request.b7 = = 'POST':
        b5 = request.form.get('currs', '').upper().replace(" ", "")
        b8 = [currency for currency in b5.split(',') if currency in b1]
        b8 = list(set(b8))
        b5 = ', '.join(b8)
        if len(b8) > 1:
            b9 = weighted_graph(b8)
            b10 = b9.show_arbitrage_opportunities()
            b11 = b9.get_time()
            b12 = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(b11))
            if len(b10) == 0:
                b6 = "No arbitrage opportunity (" + b12 + ")"
            else:
                b13 = ' -> '.join(b10[0])
                b6 = b13 + ' at ' + b12
        else:
            b6 = "No arbitrage opportunity available with less than two b14..."
    else:
        b6 = "No arbitrage opportunity available with less than two b14..."
    return render_template('home.html', b14 = b5, b1=b2, opportunity=b6)
if b15 = = '__main__':
    b3.run(b16 = True)