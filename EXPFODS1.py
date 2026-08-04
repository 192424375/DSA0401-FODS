import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read student marks from CSV file
data = pd.read_csv(r"C:\Users\joshi\Downloads\subject.csv")

# Convert to NumPy array
student_scores = data.to_numpy()

# Calculate average marks of each subject
average_scores = np.mean(student_scores, axis=0)

# Get subject names
subjects = data.columns

# Find subject with highest average
highest_index = np.argmax(average_scores)
highest_subject = subjects[highest_index]
highest_average = average_scores[highest_index]

# Display results
print("Average Score for Each Subject\n")

for subject, avg in zip(subjects, average_scores):
    print(subject, ":", round(avg, 2))

print("\nSubject with Highest Average Score:")
print(highest_subject, "-", round(highest_average, 2))

# Save result to CSV
result = pd.DataFrame({
    "Subject": subjects,
    "Average Score": average_scores
})

result.to_csv("average_scores_output.csv", index=False)

print("\nResult saved as average_scores_output.csv")

# Draw graph
plt.figure(figsize=(7,5))
plt.bar(subjects, average_scores)
plt.title("Average Score of Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

for i, value in enumerate(average_scores):
    plt.text(i, value + 1, round(value, 2), ha='center')

plt.grid(axis='y')
plt.show()
