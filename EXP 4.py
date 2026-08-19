#4. Scenario: You are working on a project that involves analyzing the sales performance of a companyover the past four quarters. The quarterly sales data is stored in a NumPy array named sales_data,
#where each element represents the sales amount for a specific quarter. Your task is to calculate thetotal sales for the year and determine the percentage increase in sales from the first quarter to the fourtquarter.
#Question: Using NumPy arrays and arithmetic operations calculate the total sales for the year anddetermine the percentage increase in sales from the first quarter to the fourth quarter?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read sales data from CSV
data = pd.read_csv(r"C:\Users\joshi\Downloads\sales.csv")

# Convert sales column to NumPy array
sales_data = data["Sales"].to_numpy()

# Calculate total sales
total_sales = np.sum(sales_data)

# Calculate percentage increase from Q1 to Q4
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

# Display results
print("Total Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4: {:.2f}%".format(percentage_increase))

# Save results to CSV
result = pd.DataFrame({
    "Description": ["Total Sales", "Percentage Increase (Q1 to Q4)"],
    "Value": [total_sales, round(percentage_increase, 2)]
})

result.to_csv("sales_analysis_output.csv", index=False)

print("\nOutput saved as sales_analysis_output.csv")

# Plot graph
quarters = data["Quarter"]

plt.figure(figsize=(7,5))
plt.plot(quarters, sales_data, marker='o')

plt.title("Quarterly Sales Performance")
plt.xlabel("Quarter")
plt.ylabel("Sales")

plt.grid(True)
plt.show()
