import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("student14.csv")

print(df)

print(df.corr())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(df["StudyHours"],df["ExamScore"])
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(df["StudyHours"],df["ExamScore"],marker="o")
plt.title("Study Time Trend")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.tight_layout()
plt.show()