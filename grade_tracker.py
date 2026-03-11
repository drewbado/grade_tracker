# Collect student data
names = []
scores = []

print("=== Student Grade Tracker ===")
print("Enter student names and scores. Type done when finished.")

# while loop to keep collecting until user types done
name = input("Enter student name (or done to stop): ")

while name != 'done':
    score = int(input("Enter score for " + name + ": "))

    # if statement to validate score range
    if score < 0 or score > 100:
        print("Score must be between 0 and 100. Try again.")
    else:
        names.append(name)
        scores.append(score)
        print(name + " added!")

    name = input("Enter student name (or done to stop): ")

print("Data entry complete. " + str(len(names)) + " students entered.")

# Process the data

total = 0
highest = scores[0]
lowest = scores[0]

# for loop with range() to walk through both lists by index
for i in range(len(names)):
    total = total + scores[i]

    if scores[i] > highest:
        highest = scores[i]

    if scores[i] < lowest:
        lowest = scores[i]

average = total / len(names)

print()
print("=== Class Summary ===")
print("Total students : " + str(len(names)))
print("Class average  : " + str(round(average, 1)))
print("Highest score  : " + str(highest))
print("Lowest score   : " + str(lowest))

print()
print("=== Full Grade Report ===")
print(f"{'Name':<20} {'Score':<8} {'Grade':<6}")
print("-" * 36)

# for loop directly over the names list
for i in range(len(names)):
    score = scores[i]

    # if/elif/else to assign letter grade
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'

    print(f"{names[i]:<20} {score:<8} {letter:<6}")