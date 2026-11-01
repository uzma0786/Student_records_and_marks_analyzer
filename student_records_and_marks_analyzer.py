Subjects = ('python','maths','DBMS')
print(f"Subject:{Subjects}")

Numbers = int(input("How many Students?"))

All_Students = {} #Empty Dictionary

for i in range(numbers):
    Student_ids = input("\nStudent_Id : ")
    Student_name = input("Name : ")
    python_marks = int(input("python marks : "))
    maths_marks = int(input("maths marks : "))
    Dbms_marks = int(input("DBMS marks : "))


    total = python_marks+maths_marks+Dbms_marks
    average_marks = total/3
    status = None
    if average_marks>=75:
        status = "Distinction"
    elif average_marks>=40:
        status = "Pass"
    else:
        status = "Fail"

    #now we are store the record in Dictionary
    all_Students[Student_ids] = {
        "name": Student_name,
        "python": python_marks,
        "maths": maths_marks,
        "Dbms": Dbms_marks,
        "Total": total,
        "Average": average_marks,
        "Status": status
    }



print("\n----- STUDENT REPORT -----")
for x in All_Students:
    y = All_Students[x]
    print(f"ID: {x} | Name: {y['name']}")
    print(f"python: {y['python']}, maths: {y['maths']}, DBMS: {y['dbms']}")
    print(f"Total: {y['total']} | Average: {y['average']:.2f} | Result: {y['status']}")
    

print(f"\nUnique subjects: {'Python','Maths','DBMS'}")
print(f"Students recorded: {Numbers}")