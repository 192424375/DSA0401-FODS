import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("likes18.csv")

print(df)

freq=df["Likes"].value_counts().sort_index()

print("\nFrequency Distribution of Likes")
print(freq)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(freq.index.astype(str),freq.values)
plt.title("Likes Frequency")
plt.xlabel("Likes")
plt.ylabel("Frequency")

plt.subplot(1,2,2)
plt.pie(freq.values,labels=freq.index,autopct="%1.1f%%")
plt.title("Likes Distribution")

plt.tight_layout()
plt.show()