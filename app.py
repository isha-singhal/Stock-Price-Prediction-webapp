from flask import Flask, render_template, request,redirect,url_for
from matplotlib import ticker
import yfinance as yf
from package import fetch

app = Flask(__name__)


#sp500 = si.tickers_sp500()

all_files = ['APPL','TSLA','AMZN']
# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route('/')
def landing_function():
    stock_files = list(all_files)
    return render_template('index.html')

@app.route('/dashboard',methods=['GET','POST'])
def dash():
    if request.method == 'POST':
        ticker = request.form["ticker"]
        info = fetch.company_info(ticker)
        return render_template('dashboard.html',info=info)
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)