student_name=input("Enter your name: ")
student_grade=int(input("Enter Your Grade:"))
base_fee=2000*student_grade
discount=0
deducted_amount=0
academic_topper=bool(input("Are you academic topper? (True/False): "))

if student_grade>=9 and student_grade<=12:
    if academic_topper:
        discount=0.20
    else:
        discount=0.10
elif(student_grade>=6 and student_grade<=8):
    discount=0.05

#Additional fee discount
if(student_grade==10):
    discount+=0.03
elif(student_grade==12):
    discount+=0.05

deducted_amount=base_fee*discount
final_fee=base_fee-deducted_amount
print(f"Student Name: {student_name}")
print(f"Student Grade: {student_grade}")
print(f"Base Fee: ${base_fee}")
print(f"Discount: {discount*100}%")
print(f"Deducted Amount: ${deducted_amount}")
print(f"Final Fee: ${final_fee}")       