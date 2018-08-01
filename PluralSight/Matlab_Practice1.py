from matplotlib import pyplot as plt
import pandas as pd

"""
plt.plot([1, 8, 5], [2 , 6, 10])
plt.plot([5, 7, 11], [4 , 8, 12])
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.title("This is my first sample plot")
plt.legend(["Data set 1", "Data Set 2"])
plt.savefig("D:\Python_Learning\Python\PluralSight\Figure_1.png")
#plt.show()
"""
data = {"Year": [2011, 2013, 2017],
        "Attendees": [112, 321, 729],
        "Average Age": [24, 43, 31]}

df = pd.DataFrame(data)
print(df["Year"])
abc = df["Year"] >= 2013

print(abc)

plt.plot(df["Year"], df["Attendees"])
plt.show()
