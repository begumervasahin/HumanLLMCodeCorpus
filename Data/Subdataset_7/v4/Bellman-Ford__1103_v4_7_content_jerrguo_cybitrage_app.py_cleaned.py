from flask import Flask, render_template, request
from b11.weighted_graph import weighted_graph
import time
b1 = ['EUR', 'USD', 'JPY', 'CHF', 'AUD', 'CAD', 'NZD', 'GBP', 'SEK', 'NOK', 'MXN', 'TRY', 'ZAR', 'CNH', 'XAU', 'XAG']
b2 = ', '.join(b1)
b3 = Flask(b16)
@b3.route('/', b4 = ['GET', 'POST'])
def fonk1():
    b5 = ""
    b6 = ""
    b7 = []
    b8 = []
    if request.b9 = = 'POST':
        b5 = request.form['currs']
        b5 = b5.upper().replace(" ", "")
        b7 = b5.split(',')
        b10 = []
        for currency in b7:
            if currency in b1:
                b10.append(currency)
        b10 = list(set(b10))
        b5 = ', '.join(b10)
        if len(b10) > 1:
            b11 = weighted_graph(b10)
            b8 = b11.show_arbitrage_opportunities()
            b12 = b11.get_time()
            b13 = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(b12))
            if len(b8) == 0:
                b6 = "No arbitrage opportunity (" + b13 + ")"
            else:
                b14 = ' -> '.join(b8[0])
                b6 = b14 + ' at ' + b13
        else:
            b6 = "No arbitrage opportunity available with less than two b15..."
    else:
        b6 = "No arbitrage opportunity available with less than two b15..."
    return render_template('home.html', b15 = b5, b1=b2, opportunity=b6)
if b16 = = '__main__':
    b3.run(b17 = True)
