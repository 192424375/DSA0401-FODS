#20. Scenario: You are a data analyst working for a marketing research company. Your team hascollected a large dataset containing customer feedback from various social media platforms. The
#dataset consists of thousands of text entries, and your task is to develop a Python program to analyzethe frequency distribution of words in this dataset. Your program should be able to perform the
#following tasks:
#• Load the dataset from a CSV file (data.csv) containing a single column named "feedback" witheach row representing a customer comment.
#• Preprocess the text data by removing punctuation, converting all text to lowercase, andeliminating any stop words (common words like "the," "and," "is," etc. that don't carrysignificant meaning).
#• Calculate the frequency distribution of words in the preprocessed dataset.
#• Display the top N most frequent words and their corresponding frequencies, where N isprovided as user input.
#• Plot a bar graph to visualize the top N most frequent words and their frequencies.
#Question: Create a Python program that fulfills these requirements and helps your team gain insightsfrom the customer feedback data.

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
