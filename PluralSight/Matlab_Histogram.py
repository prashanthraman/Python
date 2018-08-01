from matplotlib import pyplot as py
import pandas as pd

data = pd.read_csv("D:\Python_Learning\Report.csv")
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
print(data.head())

data_2015 = data[data.year == 2015]
data_2016 = data[data.year == 2016]

py.subplot(2, 1, 1)
py.xlabel("GDP per capita")
py.title("GDP per capita")
py.hist(data_2015.value, 20)
py.subplot(2, 1, 2)
py.hist(data_2016.value, 20)
py.show()
