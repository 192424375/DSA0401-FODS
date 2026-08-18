import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Read CSV file
df = pd.read_csv(r"C:\Users\bille\Downloads\21.csv")

# Calculate statistics
print("AGE AND BODY FAT ANALYSIS")
print("-------------------------")

print("\nAge")
print("Mean =", round(df["age"].mean(), 2))
print("Median =", round(df["age"].median(), 2))
print("Standard Deviation =", round(df["age"].std(), 2))

print("\nPercent Fat")
print("Mean =", round(df["percent_fat"].mean(), 2))
print("Median =", round(df["percent_fat"].median(), 2))
print("Standard Deviation =", round(df["percent_fat"].std(), 2))

# Boxplot
plt.figure(figsize=(7, 5))
plt.boxplot([df["age"], df["percent_fat"]])
plt.xticks([1, 2], ["Age", "% Fat"])
plt.title("Boxplot of Age and % Fat")
plt.ylabel("Value")
plt.grid()
plt.show()

# Scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["percent_fat"])
plt.xlabel("Age")
plt.ylabel("% Fat")
plt.title("Age vs % Fat")
plt.grid()
plt.show()

# Q-Q plot for Age
plt.figure(figsize=(6, 5))
stats.probplot(df["age"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Age")
plt.grid()
plt.show()

# Q-Q plot for Percent Fat
plt.figure(figsize=(6, 5))
stats.probplot(df["percent_fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot for % Fat")
plt.grid()
plt.show()
