import matplotlib.pyplot as plt

students = []

def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 50:
        return "B"
    else:
        return "C"

def add_student(name, marks):
    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    students.append({
        "name": name,
        "percentage": percentage,
        "grade": grade
    })

def display_students():
    print("\nStudent Report\n" + "-" * 30)
    for s in students:
        print(f"Name: {s['name']}")
        print(f"Percentage: {s['percentage']:.2f}%")
        print(f"Grade: {s['grade']}")
        print("-" * 30)

def show_charts():
    names = [s["name"] for s in students]
    percentages = [s["percentage"] for s in students]
    grades = [s["grade"] for s in students]

    # Bar Chart – Student Percentages
    plt.figure(figsize=(6, 4))
    plt.bar(names, percentages)
    plt.title("Student Performance")
    plt.ylabel("Percentage")
    plt.xlabel("Students")
    plt.tight_layout()
    plt.show()

    # Pie Chart – Grade Distribution
    grade_count = {g: grades.count(g) for g in set(grades)}

    plt.figure(figsize=(5, 5))
    plt.pie(
        grade_count.values(),
        labels=grade_count.keys(),
        autopct="%1.1f%%"
    )
    plt.title("Grade Distribution")
    plt.show()

# Sample Data
add_student("Rahul", [80, 75, 70])
add_student("Anita", [60, 55, 58])
add_student("Kiran", [45, 50, 48])

display_students()
show_charts()
