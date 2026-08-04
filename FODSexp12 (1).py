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