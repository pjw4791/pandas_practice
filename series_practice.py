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
print()

close = daeshin_day['close']
print(close)

# 키 값이 아니어서 에러
# print(daeshin_day['16.02.24'])
