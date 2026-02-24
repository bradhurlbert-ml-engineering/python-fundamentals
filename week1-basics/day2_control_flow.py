# Day 2: Control Flow - Making Decisions and Repeating Actions  
print("=" * 50)
print("PART 1: IF/ELIF/ELSE - Making Decsions")
print ("=" * 50)

#Simple if statement
age = 35
if age >= 18:
    print(f"Age {age}: You are an adult.")

# If/else
has_experience = True
if has_experience:
    print("✅Experienced developer")
else:
    print("❌ Junior developer")

# If/elif/else
years_experience = 35

if years_experience >= 20:
    print(f"{years_experience} years: Senior/Principal level")
elif years_experience >= 10:
    print(f"{years_experience} years: Senior-level")
elif years_experience >= 5:
    print(f"{years_experience} years: Mid-level")
else:
    print(f"{years_experience} years: Junior-level")

#Comparison operators
score=85
print(f"Score: {score}" )
print(f"Score > 80: {score > 80}")
print(f"Score >= 90: {score >= 90}")
print(f" Score == 85: {score == 85}")

# Combined conditions
learning_hours = 15
knows_python = True
if learning_hours >= 10 and knows_python:
    print("✅ On for ML transition ")
elif learning_hours < 10:
    print("⚠️ Need more study hours")
else:
    print("⚠️ Need to learn Python")
print()