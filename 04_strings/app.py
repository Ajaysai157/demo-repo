student_ID=int(input("Enter the student ID :"))
student_Name=input("Enter Student name :")
attendance=float(input("Enter Student attendance :"))
no_of_subjects=0
total_marks=0
continue_input="yes"
while continue_input.lower()=="yes":
    current_score=int(input("Enter the score of the subject : "))
    no_of_subjects+=1
    total_marks+=current_score
    continue_input=input("Enter 'yes' if you want to add marks of another Subject : ")

average_marks=total_marks/no_of_subjects
if average_marks>=85:
    performance="Excellent"
elif average_marks>70:
    performance="Good"
elif average_marks>50:
    performance="Average"
else:
    performance="Need Improvement"

attendance_status="Attendance is Good" if attendance>=75 else "Warning! Your attendance is low"

print("--"*50)
print(f"Student ID : {student_ID}")
print(f"Student Name : {student_Name}")
print(f"Number Of Subjects: {no_of_subjects}")
print(f"Total Marks of the student : {total_marks}")
print(f"Average Marks : {average_marks}")
print(f"Student Performance : {performance}")
print(f"Attendance Status: {attendance_status}")
print("--"*50)