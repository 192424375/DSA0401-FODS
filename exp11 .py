#11. Scenario : You are a data scientist working for a company that sells products online. You havebeen tasked with creating a simple plot to show the sales of a product over time.
#Question:
#1. Write code to create a simple line plot in Python using Matplotlib to predict sales happened in amonth?
#2. Write code to create a scatter plot in Python using Matplotlib to predict sales happened in a month?
#3. Develop a Python program to create a bar plot of the monthly sales data.

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales11.csv")

print(df)

plt.plot(df["Month"],df["Sales"],marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
