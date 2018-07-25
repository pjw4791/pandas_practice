import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()

import datetime
import matplotlib.pyplot as plt
from zipline.api import order, symbol, order_target, record
from zipline.algorithm import TradingAlgorithm

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)

data = pdr.get_data_yahoo("AAPL", start, end)
data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

# 변수 i와 sym을 context라는 네임스페이스에 추가
def initialize(context):
    # pass
    # i라는 변수는 거래일 수를 계산하는 데 사용되는 변수이고
    context.i = 0

    # sym은 참조할 데이터에 대한 심볼을 저장하는데 사용됩니다.
    context.sym = symbol('AAPL')

# 거래일마다 1주씩 매수하는 알고리즘
def handle_data(context, data):
    order(symbol('AAPL'), 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

plt.plot(result.index, result.portfolio_value)
plt.show()