import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# CSV 파일 읽기
df = pd.read_csv('python_data_A/csv_data/yp_10.csv', header=None)

# 0번째(양평읍)와 10번째(용문면) 행 추출
yangpyeong = df.iloc[0]
yongmun = df.iloc[10]

# 연령대 레이블 생성
age_labels = ['0-9세', '10-19세', '20-29세', '30-39세', '40-49세', 
             '50-59세', '60-69세', '70-79세', '80-89세', '90-99세', '100세 이상']

# 인구 데이터 추출 (3번째 열부터 마지막 열까지)
yangpyeong_pop = [int(str(x).replace(',', '')) for x in yangpyeong[3:]]
yongmun_pop = [int(str(x).replace(',', '')) for x in yongmun[3:]]

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 8))

# 막대 그래프 생성
y_pos = range(len(age_labels))
ax.barh(y_pos, yangpyeong_pop, color='skyblue', label='양평읍')
ax.barh(y_pos, [-x for x in yongmun_pop], color='lightcoral', label='용문면')

# 그래프 꾸미기
ax.set_yticks(y_pos)
ax.set_yticklabels(age_labels)
ax.set_xlabel('인구 수')
ax.set_title('양평읍과 용문면의 연령별 인구 분포')
ax.legend()

# x축 레이블 양수로 표시
xticks = ax.get_xticks()
ax.set_xticklabels([abs(int(x)) for x in xticks])

plt.tight_layout()
plt.show()