import datetime
import FinanceDataReader as fdr
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#조회 시작 날짜
# start = datetime.datetime(2018,2,19)
start = datetime.datetime(2020,3,1)
#조회 마감 날짜
# end = datetime.datetime(2018,3,4)
end = datetime.datetime(2020,3,10)

#한국거래소 상장종목 전체
# df_krx=fdr.StockListing('KRX')
#
# #리스트 10개
# # print(df_krx.head(10))
#
# #출력
# # print(df_krx['Symbol'])
# print(df_krx.iloc[0])
# print(df_krx.Symbol[0])

# print(df_krx.describe())

# 미국 APPLE 금융 정보 호출

df_app=fdr.DataReader('AAPL',start,end)
print(df_app)
# print(df_app.loc['2018-02-28'])
print(df_app.loc['2020-03-09'])

# print(df_app.describe())

# 미국 아마존
df_app=fdr.DataReader('AMGN',start,end)
print(df_app)
# print(df_app.loc['2018-02-28'])
print(df_app.loc['2020-03-09'])
# print(df_app.describe())

# 미국 구글
df_app=fdr.DataReader('GOOGL',start,end)
print(df_app)
# print(df_app.loc['2018-02-28'])
print(df_app.loc['2020-03-09'])
print(df_app.describe())





#
