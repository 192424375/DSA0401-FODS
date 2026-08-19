#26.Scenario: You are a researcher working in a medical lab, investigating the effectiveness of a newtreatment for a specific disease. You have collected data from a clinical trial with two groups: a control
#group receiving a placebo, and a treatment group receiving the new drug.Your goal is to analyze thedata using hypothesis testing and calculate the p-value to determine if the new treatment has a
#statistically significant effect compared to the placebo. You will use the matplotlib library to visualizethe data and the p-value.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
# Read CSV file
df = pd.read_csv(r"C:\Users\joshi\Downloads\26.csv")
# Separate groups
control = df[df["Group"] == "Control"]["Result"]
treatment = df[df["Group"] == "Treatment"]["Result"]
# Independent t-test
t, p = ttest_ind(control, treatment)
print("Control Mean =", round(control.mean(), 2))
print("Treatment Mean =", round(treatment.mean(), 2))
print("t-statistic =", round(t, 4))
print("p-value =", round(p, 4))
if p < 0.05:
    print("Significant difference: Reject H0")
else:
    print("No significant difference: Accept H0")

# ---------------- GRAPH 1: BOXPLOT ----------------
plt.figure(figsize=(7, 5))
plt.boxplot([control, treatment],
            tick_labels=["Control", "Treatment"])
plt.title("Control vs Treatment - Boxplot")
plt.ylabel("Result")
plt.grid(axis="y")
plt.show()

# ---------------- GRAPH 2: BAR GRAPH ----------------
plt.figure(figsize=(7, 5))
means = [control.mean(), treatment.mean()]
plt.bar(["Control", "Treatment"], means)
plt.title("Mean Result: Control vs Treatment")
plt.ylabel("Mean Result")
plt.grid(axis="y")
plt.show()

# ---------------- GRAPH 3: P-VALUE ----------------
plt.figure(figsize=(7, 5))
plt.bar(["p-value", "Significance Level"], [p, 0.05])
plt.axhline(0.05, linestyle="--", label="α = 0.05")
plt.title("Hypothesis Testing - p-value")
plt.ylabel("Value")
plt.legend()
plt.show()
