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

print("=" * 50)
print("PART 2: FOR LOOPS - Repeating Actions")
print("=" * 50)

# Loop through a range
print("Week numbers:")
for week in range(1,13):
    print(f"Week {week}")

#Loop through a list
tech_stack = ["C#", ".NET", "SQL", "Azure", "PowerShell", "Python", "PyTorch"]
print("\nTech Stack List:")
for tech in tech_stack:
    print(f"   - {tech}")

# Loop with index using enumerate
print("\nTech Stack with position:")
for index, tech in enumerate(tech_stack):
    print(f"  {index + 1}. {tech}")
    # Loop with calculations
    print("\nLearning hours per week:")
    for week in range(1,3): #Just 2 weeks for example
        print(f"Week {week}")
        for day in ["Mon, Tue","Wed", "Thu","Fri"]:
            print(f"  {day}: Code 2 hours")

# Loop with condtions
print("\nWeeks with extra effort:")
for week in range(1,13):
    if week % 2 == 0: #Every even week
        print(f"Week {week}:   20 hours (extra push!)")
    else:
        print(f"Week {week}:   15 hours")

#Break statement
print("\nLooking for PyTorch in tech stack:")
for tech in tech_stack:
    if tech == "PyTorch":
        print("Found PyTorch! Time to dive in!")
        break #stop the loop once we find PyTorch
    print(f"  Checking {tech}...")

#Continue statement
print("\nSkip weekends:")
for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    if day in ["Sat", "Sun"]:
        continue
    print(f"  {day}: Working day")

print()

print("=" * 50)
print("PART 3: WHILE LOOPS - Repeating Until a Condition is Met")
print("=" * 50) 
# Simple while loop
week = 1
while week <= 4:
    print(f"Week {week}: Keep learning!")
    week += 1

# While loop with a condition
hours_learned = 0
target_hours = 50
week = 1

print(f"\nLearning until {target_hours} hours:")
while hours_learned < target_hours:
    weekly_hours = 15
    hours_learned += weekly_hours
    print(f"Week {week}: {weekly_hours} hours (Total: {hours_learned})")
    week += 1

print(f"✅ Target of {target_hours} hours reached in {week - 1} weeks!")

#While with break
print("\nCounting until we hit 100:")
count = 0
while True: #Infinite loop, we will break out when count reaches 100
    count += 10
    print(f"Count: {count}")
    if count >= 100:
        print("✅ Reached 100!")
        break #exit loop

    #Countdown
print("\Countdown")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("🚀 Lift off!")
print()

print("=" * 50)
print("MY EXPERIMENTS")
print("=" * 50)

#Experiment 1: Yor ML learning goals
goals = [
    "Learn Python",
    "Build Neural Network from scratch",
    "Master PyTorch",
    "Get ML Engineer role"
]
print("My ML Learning Goals:")
for index, goal in enumerate(goals, start=1):
    if index <= 1:
        status = "✅ In progress"
    else:
        status = "⏳ Not started"
    print(f"{index}. {goal} - {status}")

print(f"\nPath to ML Proficiency:")
skills = {
    "Python fundamentals" : 2,
    "Neural Networks" : 2,
    "PyTorch" : 2,
    "Transformers & RAG" : 2,
    "MLOps": 4
}
total_weeks = 0
for skill, weeks in skills.items():    
    total_weeks += weeks
    print(f"  - {skill}: {weeks} weeks")
print (f"\n🎯 Total learning time: {total_weeks} weeks")
print(f"    That's {total_weeks * 15} hours of dedicated learning in this exciting journey to become an ML Engineer!")
print()
print("=" * 50)


print("\nCareer Journey:")
milestones = {
    1990: "Started in Accounting/Finance",
    1995: "Mentored by Bechtel engineers",
    2004: "Founded Hurlbert Consulting Group",
    2013: "Enterprise software engineering",
    2022: "Solutions Architect as Sprouts",
    2026: "Transition to ML/AI"
}
for year, milestone in milestones.items():
    print(f"  - {year}: {milestone}")

#Experiment 2: Calcuate a learning velocity
print("\nLearning Velocity Calculation:")
days_completed = 2
total_days = 84 #12 weeks
percent_complete = (days_completed/total_days) * 100
print(f"    Days completed: {days_completed}/{total_days} ({percent_complete:.2f}%)")
print(f"    Progress:{percent_complete:.1f}%")
print(f"    Days remaining: {total_days - days_completed}")

skills_learned = []
if percent_complete < 10:
    print("Status: Just getting started! 🌱")
elif percent_complete < 50:
    print("Status: Making solid progress! 🚀")
elif percent_complete < 75:
    print("Status: Over halfway there! 🎉")

# Experiment 3: Track skills learned each week
for week in range(1,5):
    if week == 1:
        skills_learned.append("Python basics")
    elif week == 2:
        skills_learned.append("NumPy and Pandas")
    elif week == 3:
        skills_learned.append("Neural Networks")
    elif week == 4:
        skills_learned.append("PyTorch")

print(f"    Week {week}: {', '.join(skills_learned)}")
print("🎉 Day 2 Complete! 🚀")
print("=" * 50)