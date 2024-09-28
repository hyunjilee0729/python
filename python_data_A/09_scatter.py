import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1,2,3,4], [10,30,20,40], s=[100,200,250,300], c=range(4), cmap='cool')
# plt.colorbar()

# plt.show()

import csv
x = list(range(0, 101))
y = []
size = []

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for i in data:
    if "용문면" in i[0]:
        y = i[3:]

for change in range(len(y)):
    y[change] = int(y[change])

size = y

# for i in range(100):
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))
# plt.style.use('ggplot')
# plt.scatter(x, y, s=size)

# plt.scatter(x, y, s=size, c=size, cmap='jet')

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)

plt.colorbar()
plt.show()