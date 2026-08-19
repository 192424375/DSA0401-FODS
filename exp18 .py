#18. Scenario: You are a data analyst working for a social media platform. As part of your analysis,you have a dataset containing user interaction data, including the number of likes received by each
#post. Your task is to develop a Python program that calculates the frequency distribution of likes amongthe posts.
#Question: Develop a Python program to calculate the frequency distribution of likes among the posts?

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
