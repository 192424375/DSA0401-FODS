#16. Scenario: You are working on a text analysis project and need to determine the frequencydistribution of words in a given text document. You have a text document named "sample_text.txt"
#containing a paragraph of text. Your task is to develop a Python program that reads the text document,processes the text, and generates a frequency distribution of the words.
#Question: How would you develop a Python program to calculate the frequency distribution of wordsin a text document?

from collections import Counter
import matplotlib.pyplot as plt

file=open("sample_text.txt","r")
text=file.read().lower()
file.close()

for i in ",.!?":
    text=text.replace(i,"")

words=text.split()

freq=Counter(words)

print("Word Frequency Distribution\n")
print(freq)

top=freq.most_common(10)

w=[]
c=[]

for i,j in top:
    w.append(i)
    c.append(j)

plt.figure(figsize=(8,5))

plt.bar(w,c)

plt.title("Top 10 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
