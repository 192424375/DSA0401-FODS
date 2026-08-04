import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv(r"C:\Users\joshi\Downloads\car.csv")

# Convert fuel efficiency column to NumPy array
fuel_efficiency = data["Fuel Efficiency (MPG)"].to_numpy()

# Calculate average fuel efficiency
average = np.mean(fuel_efficiency)

# Calculate percentage improvement (Model A to Model F)
old_model = fuel_efficiency[0]
new_model = fuel_efficiency[-1]

improvement = ((new_model - old_model) / old_model) * 100

# Print results
print("Average Fuel Efficiency:", round(average, 2), "MPG")
print("Percentage Improvement:", round(improvement, 2), "%")

# Save results to CSV
result = pd.DataFrame({
    "Average Fuel Efficiency (MPG)": [round(average, 2)],
    "Percentage Improvement (%)": [round(improvement, 2)]
})

result.to_csv("fuel_efficiency_result.csv", index=False)

print("Result saved as fuel_efficiency_result.csv")

# Plot Graph
plt.figure(figsize=(8,5))
plt.bar(data["Car Model"], fuel_efficiency)
plt.title("Fuel Efficiency of Car Models")
plt.xlabel("Car Model")
plt.ylabel("Fuel Efficiency (MPG)")
plt.grid(axis='y')
plt.show()
