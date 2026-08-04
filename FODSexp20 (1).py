import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

df=pd.read_csv("data20.csv")

print(df)

stopwords={"the","is","and","to","of","a","an","in","on","for","this","was","i"}

text=" ".join(df["feedback"]).lower()

for i in ",.!?":
    text=text.replace(i,"")

words=[]

for w in text.split():
    if w not in stopwords:
        words.append(w)

freq=Counter(words)

print("\nFrequency Distribution")
print(freq)

n=int(input("Enter Top N Words: "))

top=freq.most_common(n)

word=[]
count=[]

for i,j in top:
    word.append(i)
    count.append(j)

print("\nTop",n,"Words")

for i,j in top:
    print(i,":",j)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.bar(word,count)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.subplot(1,2,2)
plt.pie(count,labels=word,autopct="%1.1f%%")
plt.title("Word Distribution")

plt.tight_layout()
plt.show()