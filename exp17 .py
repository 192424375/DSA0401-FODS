#17. Scenario: You are a data analyst working for a company that sells products online. You have beentasked with analyzing the sales data for the past month. The data is stored in a Pandas data frame.
#Question: Develop a code in python to find the frequency distribution of the ages of the customers whohave made a purchase in the past month.

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("customers17.csv")

print(df)

freq=df["Age"].value_counts().sort_index()

print("\nFrequency Distribution")
print(freq)

plt.figure(figsize=(8,5))

plt.bar(freq.index.astype(str),freq.values)

plt.title("Age Frequency Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
