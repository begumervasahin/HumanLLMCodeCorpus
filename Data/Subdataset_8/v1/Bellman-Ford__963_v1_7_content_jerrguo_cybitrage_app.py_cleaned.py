from flask import Flask, render_template, request
from graph.weighted_graph import weighted_graph
import time
support_currs = ['EUR', 'USD', 'JPY', 'CHF', 'AUD', 'CAD', 'NZD', 'GBP', 'SEK', 'NOK', 'MXN', 'TRY', 'ZAR', 'CNH', 'XAU', 'XAG']
support_currs_string = ', '.join(support_currs)
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def currencies():
    currencies_string = ""
    opportunity_string = ""
    if request.method == 'POST':
        currencies_string = request.form.get('currs', '').upper().replace(" ", "")
        curr_list = [currency for currency in currencies_string.split(',') if currency in support_currs]
        curr_list = list(set(curr_list))
        currencies_string = ', '.join(curr_list)
        if len(curr_list) > 1:
            graph = weighted_graph(curr_list)
            opportunities = graph.show_arbitrage_opportunities()
            time_epoch = graph.get_time()
            time_string = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(time_epoch))
            if len(opportunities) == 0:
                opportunity_string = "No arbitrage opportunity (" + time_string + ")"
            else:
                opp_string = ' -> '.join(opportunities[0])
                opportunity_string = opp_string + ' at ' + time_string
        else:
            opportunity_string = "No arbitrage opportunity available with less than two currencies..."
    else:
        opportunity_string = "No arbitrage opportunity available with less than two currencies..."
    return render_template('home.html', currencies=currencies_string, support_currs=support_currs_string, opportunity=opportunity_string)
if __name__ == '__main__':
    app.run(debug=True)