from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

class Zakat_calculator:
    def __init__(self, total_zakat=0):
        self.total_zakat = total_zakat

    def calculation(self, gold, gold_rate, silver, silver_rate, inventory, cash, loan):
        zakat = ((gold * gold_rate) + (silver * silver_rate) + inventory + cash - loan) / 40
        self.total_zakat = zakat
        return self.total_zakat

item = Zakat_calculator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gold_input = float(request.form['gold'])
        gold_rate_input = float(request.form['gold_rate'])
        silver_input = float(request.form['silver'])
        silver_rate_input = float(request.form['silver_rate'])
        inventory_input = float(request.form['inventory'])
        cash_input = float(request.form['cash'])
        loan_input = float(request.form['loan'])
        item.calculation(gold_input, gold_rate_input, silver_input, silver_rate_input, inventory_input, cash_input, loan_input)
        return render_template('index1.html', item = item)
    else:
        return render_template('index.html', item = item)

    

if __name__ == '__main__':
    app.run(debug=True)