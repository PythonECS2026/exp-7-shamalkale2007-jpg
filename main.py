# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder:Shamal 
# Date:4/2/26

print("--- Student Records Manager ---")
students_records = {
    "251P005" : {"name":"Sameer","grade":"A","attendance": 68},
    "251P055" : {"name":"Abdulla","grade":"B+","attendance": 88},
    "251P026" : {"name":"Katrina","grade":"A-","attendance": 55},
}

# -------- Add a New Student --------
uin = input("Enter New Student UIN: ")
name = input("Enter New Student Name: ")
grade = input("Enter New Student Grade: ")
attendance = int(input("Enter New Student Attendance: "))

students_records[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

# -------- Update Grade of a Student --------
update_uin = input("Enter UIN to Update: ")
new_grade = input("Enter New Grade of Student: ")
students_records[update_uin]["grade"] = new_grade

# -------- Delete a Student --------
delete_uin = input("Enter UIN of the Student to Delete: ")
delete students_records[delete_uin]


# Stop coding here
print(f"Final Student Records: {students_records}")




