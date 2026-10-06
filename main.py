import numpy as np

students = np.array(["A", "B", "C", "D", "E"])

subjects = np.array(["Maths", "Python", "ML", "English"])

marks = np.array([
    [80, 85, 78, 75], 
    [65, 70, 68, 72],  
    [90, 92, 88, 85],  
    [55, 60, 58, 65],  
    [75, 80, 72, 78]
])
print("================================")
print("STUDENT PERFORMANCE REPORT")
print("================================")

print("\n")

print("Total Students:", students.shape)
print("Total Subjects:", subjects.shape)
print("\n")
print("Subject Analysis")
print("--------------------------------")
#highest average marks
avgmarks = np.mean(marks, axis=0)
print("Best Average Subject:", subjects[np.argmax(avgmarks)])

#Median
mediann = np.median(marks, axis=0)
print("Median marks:", mediann)

#Mode
value, count = np.unique(marks, return_counts=True)
mode = value[np.argmax(count)]
print("Mode:", mode)

#Variance
variance = np.var(marks, axis=0)
print("Highest Variance:", subjects[np.argmax(variance)], max(variance))

#Standard Deviation
std = np.std(marks, axis=0)
print("Most consistent subject:", subjects[np.argmin(std)])
print("\n")
print("Correlation")
print("--------------------------------")
#Correlation
mathm = marks[:, 0]
pythonm = marks[:, 1]
ml = marks[:, 2]

math_py = np.corrcoef(mathm, pythonm)[0, 1]
math_ml= np.corrcoef(mathm, ml)[0, 1]

def correlation(cor):
    if cor >= 0.7:
        return "Strong Positive Correlation"

    elif cor >= 0.3:
        return "Moderate Positive Correlation"

    elif cor > -0.3:
        return "Weak or No Correlation"

    elif cor > -0.7:
        return "Moderate Negative Correlation"

    else:
        return "Strong Negative Correlation"

print("Maths ↔ Python:", correlation(math_py))
print("Maths ↔ ML:", correlation(math_ml))

print("\n")
print("Student Analysis")
print("-----------------------------")
student_avg = np.mean(marks, axis=1)
for i in range(len(students)):
    avg = student_avg[i]
    if avg >= 85:
        performance = "Excellent"
    elif avg >= 75:
        performance = "Good"
    elif avg >= 65:
        performance = "Average"
    else:
        performance = "Needs Improvement"
    print(f"\nStudent {students[i]}")
    print(f"Overall Performance: {performance}")

print("\n")
print("Performance Trend")
print("-------------------------")
def performance_trend(marks):
    changes = np.diff(marks)
    if np.all(changes > 0):
        return "Improving"

    elif np.all(changes == 0):
        return "Stable"

    elif np.all(changes < 0):
        return "Decreasing"

    else:
        return "Fluctuating"
    
for i in range(len(students)):
    trend = performance_trend(marks[i])
    print(f"Student {students[i]}: {trend}")