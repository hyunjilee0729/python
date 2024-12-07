import matplotlib.pyplot as plt
import csv

f = open('python_data_A/csv_data/yp1.csv', 'r', encoding='utf-8')
data = csv.reader(f)
result = []

# for row in data:
#     if '용문면' in row[0]:
#         for i in row[3:]:
#             if ',' in i:
#                 i = i.replace(',', '')
#             result.append(int(i))

# plt.bar(range(len(result)), result)
# # plt.barh(range(len(result)), result)
# plt.show()

yp_all = []
label_ages = ["0~9", "10~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~99", "100~"]
yp_gen = []
label_ages = ["0~19", "20~39", "40~59", "60~"]

for i in data:
    yp_all.append(i)

for da in range(len(yp_all)):
    for change in range(len(yp_all[da][3:])):
        if "," in yp_all[da][change + 3]:
            yp_all[da][change + 3] = int(yp_all[da][change + 3].replace(",", ""))
        else:
            yp_all[da][change + 3] = int(yp_all[da][change + 3])
        
plt.pie(yp_all[10][3:], labels=label_ages, autopct="%.1f%%")
plt.show()

