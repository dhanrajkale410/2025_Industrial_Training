# Assignment 7: Array (List) Program: 
# Task: Create a program that:
# Stores daily temperatures in a list
# Finds the hottest/coldest day
# Calculates days above average
# Demonstrates list slicing

# Store daily temperatures in a list
temperatures = [30, 32, 35, 28, 31, 33, 29]

# Find the hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)

print(f"Hottest temperature: {hottest}°C")
print(f"Coldest temperature: {coldest}°C")

# Calculate the average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.2f}°C")

# Calculate days above average
days_above_avg = [temp for temp in temperatures if temp > average_temp]
print(f"Number of days above average: {len(days_above_avg)}")
print(f"Temperatures above average: {days_above_avg}")

# Demonstrate list slicing
# For example, get temperatures for mid-week (e.g., days 2 to 5)
mid_week_temps = temperatures[1:5]  # index 1 to 4
print(f"Mid-week temperatures (sliced list): {mid_week_temps}")