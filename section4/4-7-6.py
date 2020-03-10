import datetime
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import io
import sys

from matplotlib import font_manager, rc

font_info='c:/windows/fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_info).get_name()
rc('font',family=font_name)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#matplotlib_converters: 날짜(시간)관련 Warning 제거
register_matplotlib_converters()    #참고

#조회 시작 날짜
start = datetime.datetime(2020,3,4)
#조회 마감 날짜
end = datetime.datetime(2020,3,10)
#네이버 주식 정보 조회
gs_naver = fdr.DataReader('035420',start,end)
#카카오 주식 정보 조회
gs_daum = fdr.DataReader('035720',start,end)
#중간출력
        # print(gs_naver)
        # print(gs_daum)
#차트 윈도우 제목
fig = plt.figure('Chart Test')
#차트 사이즈 설정
fig.set_size_inches(7,6,forward=True)
#차트 설정1
plt.plot(gs_naver.index, gs_naver['Close'], 'r', label="Naver")   # x,y 값 설정
#차트 설정2
plt.plot(gs_daum.index, gs_daum['Close'], 'y', label="Kakao")   # x,y 값 설정
#범례
plt.legend(loc='right upper')
#차트 제목
plt.title('Naver & Daum')
#x축 레이블
plt.xlabel('일자')
#y축 레이블
plt.ylabel('종가')
#차트 실행
plt.show()

# a=gs_naver['close']
# b=gs_daum['close']
