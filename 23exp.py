import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Read CSV file
df = pd.read_csv(r"C:\Users\bille\Downloads\23.csv")

# Separate the two designs
A = df[df["design"] == "A"]["conversion_rate"]
B = df[df["design"] == "B"]["conversion_rate"]

# Calculate means
mean_A = A.mean()
mean_B = B.mean()

# Perform independent t-test
t_value, p_value = ttest_ind(A, B, equal_var=False)

# Display results
print("A/B TEST ANALYSIS")
print("-----------------")

print("\nDesign A")
print("Mean Conversion Rate =", round(mean_A, 3))

print("\nDesign B")
print("Mean Conversion Rate =", round(mean_B, 3))

print("\nT-Test Results")
print("t-value =", round(t_value, 3))
print("p-value =", round(p_value, 4))

# Decision
if p_value < 0.05:
    print("\nConclusion:")
    print("There is a statistically significant difference")
    print("between Design A and Design B.")
else:
    print("\nConclusion:")
    print("There is no statistically significant difference")
    print("between Design A and Design B.")

# Graph 1: Bar chart
plt.figure(figsize=(7, 5))
plt.bar(["Design A", "Design B"], [mean_A, mean_B])
plt.title("Average Conversion Rate")
plt.ylabel("Conversion Rate")
plt.grid(axis="y")
plt.show()

# Graph 2: Boxplot
plt.figure(figsize=(7, 5))
plt.boxplot([A, B])
plt.xticks([1, 2], ["Design A", "Design B"])
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.grid()
plt.show()
