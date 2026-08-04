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