from flask import Flask, render_template, request
from graph.weighted_graph import weighted_graph
import time
SUPPORTED_CURRENCIES = ['EUR', 'USD', 'JPY', 'CHF', 'AUD', 'CAD', 'NZD', 'GBP', 'SEK', 'NOK', 'MXN', 'TRY', 'ZAR', 'CNH', 'XAU', 'XAG']
SUPPORTED_CURRENCIES_STRING = ', '.join(SUPPORTED_CURRENCIES)
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def currencies():
    selected_currencies = ""
    arbitrage_opportunity = ""
    if request.method == 'POST':
        selected_currencies = request.form.get('currs', '').upper().replace(" ", "")
        selected_currencies = ', '.join(set(curr for curr in selected_currencies.split(',') if curr in SUPPORTED_CURRENCIES))
        if len(selected_currencies) > 1:
            graph = weighted_graph(selected_currencies.split(', '))
            opportunities = graph.show_arbitrage_opportunities()
            time_epoch = graph.get_time()
            time_string = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time_epoch))
            if len(opportunities) == 0:
                arbitrage_opportunity = f"No arbitrage opportunity ({time_string})"
            else:
                opp_string = ' -> '.join(opportunities[0])
                arbitrage_opportunity = f"{opp_string} at {time_string}"
        else:
            arbitrage_opportunity = "No arbitrage opportunity available with less than two currencies..."
    else:
        arbitrage_opportunity = "No arbitrage opportunity available with less than two currencies..."
    return render_template('home.html', currencies=selected_currencies, support_currs=SUPPORTED_CURRENCIES_STRING, opportunity=arbitrage_opportunity)
if __name__ == '__main__':
    app.run(debug=True)
