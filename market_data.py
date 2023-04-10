import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    yesterdays_data = stock.history(period='2d').iloc[-2]

    current_price = todays_data['Close'].iloc[-1]
    previous_price = yesterdays_data['Close']
    percent_change = ((current_price - previous_price) / previous_price) * 100

    return current_price, percent_change

def get_market_data():
    indices = {
        'S&P 500': '^GSPC',
        'Dow Jones': '^DJI',
        'Nasdaq': '^IXIC'
    }

    data = {}
    for index_name, ticker in indices.items():
        current_price, percent_change = get_stock_data(ticker)
        data[index_name] = {
            'current_price': current_price,
            'percent_change': percent_change
        }

    return data
