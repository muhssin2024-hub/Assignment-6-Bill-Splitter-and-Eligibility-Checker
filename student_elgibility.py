def student_eligibility_test(marks, attendance, has_fee_balance):
    return (marks >= 70 and attendance >= 0.80 and not has_fee_balance) or marks >= 90


marks = float(input("Enter student marks: "))
choice = input("Add another mark in student_eligibility_test? (yes/no): ")
marks = input("enter an other marks ")
attendance = float(input("Enter attendance as a decimal (for example, 0.80): "))

has_fee_balance = input("Has fee balance? (yes/no): ").strip().lower() == "yes"

print(student_eligibility_test(marks, attendance, has_fee_balance))
student_eligibility_test(marks, attendance, has_fee_balance)

