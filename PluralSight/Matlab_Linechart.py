from matplotlib import pyplot as py
import pandas as pd
import numpy as ny

data = pd.read_csv("D:\Python_Learning\Report.csv")
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
print(data.head())

data_css = data[data.country_code == 'CSS']
data_ceb = data[data.country_code == 'CEB']
"""
py.xlabel("Year")
py.ylabel("GDP Value")
py.title("GDP ratio comparison of Caribbean small states & Central Europe")
py.plot(data_css.year, data_css.value)
py.plot(data_ceb.year, data_ceb.value)
py.legend(["Central Europe", "Caribbean"])
py.show()
"""
data_css_growth = data_css.value/data_css.value.iloc[0]*100
data_ceb_growth = data_ceb.value/data_ceb.value.iloc[0]*100
py.plot(data_css.year, data_css_growth)
py.plot(data_ceb.year, data_ceb_growth)
py.legend(["Central Europe", "Caribbean"])
py.show()
