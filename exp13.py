#13. Scenario: You are a data analyst working for a finance company. Your team is interested inanalyzing the variability of stock prices for a particular company over a certain period. The company's
#stock data includes the closing prices for each trading day of the specified period.Question: Your task is to build a Python program that reads the stock data from a CSV file, calculates
#the variability of stock prices, and provides insights into the stock's price movements.

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("stock13.csv")

print(df)

print("Mean =",df["ClosingPrice"].mean())
print("Variance =",df["ClosingPrice"].var())
print("Standard Deviation =",df["ClosingPrice"].std())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(df["Day"],df["ClosingPrice"],marker="o")
plt.title("Stock Closing Price")
plt.xlabel("Day")
plt.ylabel("Price")
plt.grid(True)

plt.subplot(1,2,2)
plt.boxplot(df["ClosingPrice"])
plt.title("Stock Price Variability")
plt.ylabel("Price")

plt.tight_layout()
plt.show()
