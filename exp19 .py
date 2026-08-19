#19. Scenario: You are working on a project that involves analyzing customer reviews for a product.You have a dataset containing customer reviews, and your task is to develop a Python program that
#calculates the frequency distribution of words in the reviews.Question: Develop a Python program to calculate the frequency distribution of words in the customer
#reviews dataset?

import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df=pd.read_csv("reviews19.csv")

print(df)

text=" ".join(df["Review"]).lower()

for i in ",.!?":
    text=text.replace(i,"")

words=text.split()

freq=Counter(words)

print("\nWord Frequency")
print(freq)

top=freq.most_common(10)

w=[]
c=[]

for i,j in top:
    w.append(i)
    c.append(j)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(w,c)
plt.title("Top 10 Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.subplot(1,2,2)
plt.pie(c,labels=w,autopct="%1.1f%%")
plt.title("Word Distribution")

plt.tight_layout()
plt.show()
