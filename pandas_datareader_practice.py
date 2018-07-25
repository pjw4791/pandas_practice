import pandas_datareader.data as pdr
import datetime
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

start = datetime.datetime(2016, 1, 1)

end = datetime.datetime(2018, 7, 23)

# due to the yahoo API update, currently not working
# gs = pdr.DataReader("078930.KS", "yahoo", start, end)
# print(gs)

# due to the google API update, currently not working
# KOSPI = pdr.DataReader("KRX:KOSPI", "google", start, end)


# data = pdr.get_data_yahoo("AAPL", start, end)
# print(data)

# plt.plot(data.index, data['Adj Close'])
# plt.show()

gs = pdr.get_data_yahoo("078930.KS", start, end)
# gs = pdr.get_data_yahoo("078930.KS")

# remove holiday
# HOWEVER, how can I catch the zero volume day when is not a holiday.
new_gs = gs[gs['Volume'] !=0]
# print(gs)
# print(gs.info())
# plt.plot(gs.index, gs['Adj Close'])
# plt.show()

# only print recent 5 days
print(gs.tail())

ma5 = gs['Adj Close'].rolling(window=5).mean()
print(type(ma5))
print(ma5.tail(10))

new_gs.insert(len(new_gs.columns), "MA5", ma5)
print(new_gs.tail(5))

ma20 = new_gs['Adj Close'].rolling(window=20).mean()

ma60 = new_gs['Adj Close'].rolling(window=60).mean()

ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), "MA20", ma20)

new_gs.insert(len(new_gs.columns), "MA60", ma60)

new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

# 범례를 표시하기 위해 legend 함수를 호출합니다.
# 이때 loc 인자를 통해 범례 표시 위치를 지정할 수 있습니다.
# 범례가 적절한 위치에 자동으로 출력되게 하려면 loc='best' 옵션을 사용하면 됩니다.
# 또한 그래프의 값을 좀 더 편리하게 확인하기 위한 격자(grid)를 표시하려면 grid 함수를 호출하면 됩니다.
plt.legend(loc='best')
plt.grid()
plt.title("GS adjusted price and MA5,20,60,120")
plt.show()
