import yfinance as yf

def company_info(ticker):
    tick = yf.Ticker(ticker)
    return tick.info

