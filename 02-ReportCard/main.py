# 3 subjts marks
# Grades
# Report
mathematics_marks : int = int(input("Enter Your marks of Mathematics: "))
english_marks : int = int(input("Enter Your marks English: "))
science_marks : int = int(input("Enter Your marks Science: "))
  
def calculate_grade(marks):
    if(marks < 0 or marks > 100):
        return "InvaliD Input! Enter marks between 0 to 100"
    elif marks > 75:
        return "Grade A"
    elif marks > 50:
        return "Grade B"
    elif marks > 33:
        return "Grade C"
    elif marks > 0:
        return "Grade F"
    else:
        return "Invalid Input"

math_grade = calculate_grade(mathematics_marks)
english_grade = calculate_grade(english_marks)
science_grade = calculate_grade(science_marks)

print(f"You have got {mathematics_marks} marks in Mathematics and You got {math_grade} grade.")
print(f"You have got {english_marks} marks in English and You got {english_grade} grade.")
print(f"You have got {science_marks} marks in Science and You got {science_grade} grade.")

print(f"""
      +--------------------------------------------------------------+
      |--------------------|--------------------|--------------------|
      |______Subject_______|_______Marks________|_______Grade________|
      |_____Mathematics____|__________{mathematics_marks}________|_______{math_grade}______|
      |_______English______|__________{english_marks}________|_______{english_grade}______|
      |_______Science______|__________{science_marks}________|_______{science_grade}______|
      |--------------------------------------------------------------|
      +--------------------------------------------------------------+
      """)