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