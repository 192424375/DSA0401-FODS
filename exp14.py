#14. Scenario: You are a data scientist working for an educational institution, and you want to explorethe correlation between students' study time and their exam scores. You have collected data from a
#group of students, noting their study time in hours and their corresponding scores in an exam.Question: Identify any potential correlation between study time and exam scores and explore various
#plotting functions to visualize this relationship effectively.

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
