import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read CSV file
df = pd.read_csv(r"C:\Users\bille\Downloads\22.csv")

# Separate groups
drug = df[df["group"] == "Drug"]["reduction"]
placebo = df[df["group"] == "Placebo"]["reduction"]

# Function for 95% confidence interval
def confidence_interval(data):
    mean = data.mean()
    n = len(data)
    sd = data.std()

    t_value = stats.t.ppf(0.975, n - 1)
    margin = t_value * sd / (n ** 0.5)

    return mean, mean - margin, mean + margin

# Calculate confidence intervals
drug_mean, drug_low, drug_high = confidence_interval(drug)
placebo_mean, placebo_low, placebo_high = confidence_interval(placebo)

# Display results
print("BLOOD PRESSURE CONFIDENCE INTERVAL")
print("----------------------------------")

print("\nDrug Group")
print("Mean Reduction =", round(drug_mean, 2))
print("95% CI =", round(drug_low, 2), "to", round(drug_high, 2))

print("\nPlacebo Group")
print("Mean Reduction =", round(placebo_mean, 2))
print("95% CI =", round(placebo_low, 2), "to", round(placebo_high, 2))

# Graph 1: Confidence Interval
means = [drug_mean, placebo_mean]

lower = [drug_mean - drug_low,
         placebo_mean - placebo_low]

upper = [drug_high - drug_mean,
         placebo_high - placebo_mean]

plt.figure(figsize=(7, 5))
plt.errorbar(
    ["Drug", "Placebo"],
    means,
    yerr=[lower, upper],
    fmt="o",
    capsize=6
)

plt.title("Mean Reduction with 95% Confidence Interval")
plt.ylabel("Blood Pressure Reduction")
plt.grid()
plt.show()

# Graph 2: Boxplot
plt.figure(figsize=(7, 5))
plt.boxplot([drug, placebo])
plt.xticks([1, 2], ["Drug", "Placebo"])
plt.title("Blood Pressure Reduction")
plt.ylabel("Reduction")
plt.grid()
plt.show()
