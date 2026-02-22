# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student 
# including their grades and attendance.
# Coder: Shamal
# Date: 4/2/26

# Write uin = input("Enter New Student UIN: ")
name = input("Enter New Student Name: ")
grade = input("Enter New Student Grade: ")
attendance = int(input("Enter New Student Attendance: "))

students_records[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

#Update the Grade of Student of UIN 251P055
update_uin = input("Enter UIN to Update: ")
new_grade = input("Enter New Grade of Student: ")
students_records[update_uin]["grade"] = new_grade

#Remove Student with UIN 251P026
delete_uin = input("Enter UIN of the Student to Delete: ")
delete students_records[delete_uin]e your code here
# TODO: Add a new Student Record 
uin = input("Enter New Student UIN: ")
name = input("Enter New Student Name: ")
grade = input("Enter New Student Grade: ")
attendance = int(input("Enter New Student Attendance: "))

students_records[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}
# TODO: Update the Grade of Student of UIN 251P005
update_uin = input("Enter UIN to Update: ")
new_grade = input("Enter New Grade of Student: ")
students_records[update_uin]["grade"] = new_grade
# TODO: Remove Student with UIN 251P055
delete_uin = input("Enter UIN of the Student to Delete: ")
delete students_records[delete_uin]e your code here






