import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()

import datetime
import matplotlib.pyplot as plt
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)

data = pdr.get_data_yahoo("AAPL", start, end)
data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()