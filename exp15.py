#15. Scenario: You work for a weather data analysis company, and your team is responsible fordeveloping a program to calculate and analyze variability in temperature data for different cities.
#Question: Write a python program will take in a dataset containing daily temperature readings for eachcity over a year and perform the following tasks:
#1. Calculate the mean temperature for each city.
#2. Calculate the standard deviation of temperature for each city.
#3. Determine the city with the highest temperature range (difference between the highest and lowest#temperatures).
#4. Find the city with the most consistent temperature (the lowest standard deviation).

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("temperature15.csv")

print(df)

mean=df.groupby("City")["Temperature"].mean()
std=df.groupby("City")["Temperature"].std()
r=df.groupby("City")["Temperature"].max()-df.groupby("City")["Temperature"].min()

print("\nMean Temperature")
print(mean)

print("\nStandard Deviation")
print(std)

print("\nTemperature Range")
print(r)

print("\nCity with Highest Range")
print(r.idxmax())

print("\nMost Consistent City")
print(std.idxmin())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
mean.plot(kind="bar")
plt.title("Mean Temperature")
plt.ylabel("Temperature")
plt.grid(True)

plt.subplot(1,2,2)
r.plot(kind="bar")
plt.title("Temperature Range")
plt.ylabel("Range")
plt.grid(True)

plt.tight_layout()
plt.show()
