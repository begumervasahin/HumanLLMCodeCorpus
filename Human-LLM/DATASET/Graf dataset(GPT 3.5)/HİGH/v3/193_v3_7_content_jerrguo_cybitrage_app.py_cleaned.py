from flask import Flask, render_template, request
from b8.weighted_graph import weighted_graph
import time
b1 = ['EUR', 'USD', 'JPY', 'CHF', 'AUD', 'CAD', 'NZD', 'GBP', 'SEK', 'NOK', 'MXN', 'TRY', 'ZAR', 'CNH', 'XAU', 'XAG']
b2 = ', '.join(b1)
b3 = Flask(b14)
@b3.route('/', b4 = ['GET', 'POST'])
def fonk1():
    b5 = ""
    b6 = ""
    if request.b7 = = 'POST':
        b5 = request.form.get('currs', '').upper().replace(" ", "")
        b5 = ', '.join(set(curr for curr in b5.split(',') if curr in b1))
        if len(b5) > 1:
            b8 = weighted_graph(b5.split(', '))
            b9 = b8.show_arbitrage_opportunities()
            b10 = b8.get_time()
            b11 = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(b10))
            if len(b9) == 0:
                b6 = f"No arbitrage opportunity ({b11})"
            else:
                b12 = ' -> '.join(b9[0])
                b6 = f"{b12} at {b11}"
        else:
            b6 = "No arbitrage opportunity available with less than two b13..."
    else:
        b6 = "No arbitrage opportunity available with less than two b13..."
    return render_template('home.html', b13 = b5, support_currs=b2, opportunity=b6)
if b14 = = '__main__':
    b3.run(b15 = True)
