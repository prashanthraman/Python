from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("D:\Python_Learning\Train_Time.csv")
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
data_mas = data[data.station_code == 'MAS']


data_bang = data_mas[data.station_code == 'SBC']

print(set(data.distance.max()))

plt.hist(data_mas.distance, 24, range=(0, 24))
plt.show()

plt.hist()