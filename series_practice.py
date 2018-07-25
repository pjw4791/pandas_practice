from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print("kakao\n", kakao)
print()

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print("merge\n", merge)
print()

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print(daeshin_day)
print(type(daeshin_day))
print()
#            open   high    low  close
# 16.02.29  11650  12100  11600  11900
# 16.02.26  11100  11800  11050  11600
# 16.02.25  11200  11200  10900  11000
# 16.02.24  11100  11100  10950  11100
# 16.02.23  11000  11150  10900  11050
# <class 'pandas.core.frame.DataFrame'>



close = daeshin_day['close']
print(close)
print(type(close))
print()
# 16.02.29    11900
# 16.02.26    11600
# 16.02.25    11000
# 16.02.24    11100
# 16.02.23    11050
# Name: close, dtype: int64
# <class 'pandas.core.series.Series'>

# 키 값이 아니어서 에러
# print(daeshin_day['16.02.24'])

day_data = daeshin_day.ix['16.02.24']
print(day_data)
print(type(day_data))
print()
# open     11100
# high     11100
# low      10950
# close    11100
# Name: 16.02.24, dtype: int64
# <class 'pandas.core.series.Series'>

print(daeshin_day.columns)
print(daeshin_day.index)
# Index(['open', 'high', 'low', 'close'], dtype='object')
# Index(['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23'], dtype='object')