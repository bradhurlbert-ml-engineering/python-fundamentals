# Day 1: Python Basics - Variables, Strings, Numbers

# Variables
name = "Brad Hurlbert"
years_experience = 41
current_role = "Solutions Architect"
learning = "Python for ML"
target_role = "ML Engineer"

print("=" * 50)
print("MY PYTHON JOURNEY")
print("=" * 50)
print(f"Name: {name}")
print(f"Experience: {years_experience} years")
print(f"Current Role: {current_role}")
print(f"Target Role: {target_role}")
print(f"Learning: {learning}")
print()

# String operations
old_stack = "C#, .NET, SQL, Azure, PowerShell"
new_stack = old_stack + ", Python, PyTorch"

print("Tech Stack Evolution:")
print(f"Before: {old_stack}")
print(f"After: {new_stack}")
print()

# Numbers and basic math
weeks_to_learn = 12
hours_per_week = 15
total_hours = weeks_to_learn * hours_per_week

print("Learning Plan:")
print("Python Math:")
print(f" 10/3 = {10/3}")  #Division (float)
print(f" 10//3 = {10//3}") # Floor division (int)
print(f" 10%3 = {10%3}") # Modulo (remainder)
print(f" 2 ** 8 = {2 ** 8}") # Exponentiation
print()

#Type checking
print("Variable Types:")
print(f"name: {type(name)}")
print(f"years_experience: {type(years_experience)}")
print(f"total_hours: {type(total_hours)}")
print()

print("=" * 50)
print("Day 1 Complete! ")
print("=" * 50)
