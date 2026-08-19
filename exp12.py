#12. Scenario: You are working on a data analysis project that involves analyzing the monthlytemperature and rainfall data for a city. You have a dataset containing the monthly temperature and
#rainfall values for each month of a year. Your task is to develop a Python program that generates lineplots and scatter plots to visualize the temperature and rainfall data.
#Question:
#1. Develop a Python program to create a line plot of the monthly temperature data.
#2: Develop a Python program to create a scatter plot of the monthly rainfall data.

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather12.csv")

print(df)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(df["Month"],df["Temperature"],marker="o")
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(df["Month"],df["Rainfall"])
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.grid(True)

plt.tight_layout()
plt.show()
