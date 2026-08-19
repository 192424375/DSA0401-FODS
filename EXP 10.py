#10. Scenario: You are working on a data visualization project and need to create basic plots usingMatplotlib. You have a dataset containing the monthly sales data for a company, including the month
#and corresponding sales values. Your task is to develop a Python program that generates line plots andbar plots to visualize the sales data.
#Question:1. How would you develop a Python program to create a line plot of the monthly sales data?2: How would you develop a Python program to create a bar plot of the monthly sales data?

import pandas as pd
import matplotlib.pyplot as plt

# Enter CSV file path
file_path = input("Enter the CSV file path: ")

# Read CSV file
sales = pd.read_csv(file_path)

print("\nMonthly Sales Data")
print(sales)

# -------- Line Plot --------
plt.figure(figsize=(7,5))

plt.plot(sales["Month"], sales["Sales"], marker="o", color="blue")

plt.title("Monthly Sales Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# -------- Bar Plot --------
plt.figure(figsize=(7,5))

plt.bar(sales["Month"], sales["Sales"], color="green")

plt.title("Monthly Sales Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
