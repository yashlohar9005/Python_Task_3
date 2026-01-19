def calculate_grade(marks):
    # Check for invalid marks
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."

    # Nested conditions to simulate real rules
    if marks >= 90 and marks <= 100:
        return "Grade: A+ (Excellent)"
    elif marks >= 80 and marks < 90:
        return "Grade: A (Very Good)"
    elif marks >= 70 and marks < 80:
        return "Grade: B (Good)"
    elif marks >= 60 and marks < 70:
        return "Grade: C (Average)"
    elif marks >= 50 and marks < 60:
        return "Grade: D (Pass)"
    else:
        return "Grade: F (Fail)"


# Main Program
print("===== Grade Calculator =====")

try:
    marks = float(input("Enter your marks (0 to 100): "))
    result = calculate_grade(marks)
    print("\nResult:", result)

except ValueError:
    print("Invalid input! Please enter numeric marks only.")
