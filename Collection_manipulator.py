print("==============================")
print("STUDENT DATA ORGANIZER")
print("==============================")
print("Welcome to Student Data Organizer!")
print("This program is used to manage Student records")
print("You can add, display, update and delete student records.")
print("You can also view all unique subjects offered")
print("================================")

#List to store all student records
all_students = []

#set to store unique subjects
unique_subjects = set()

#Dictionary to store student data using Student ID as key
student_data = {}

while True:
    print("==========MENU==========")
    print("1. Add Student")
    print("2. Display All student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Student Subject Offered")
    print("6. Exit")
    print("==========================")

    choice = input("Enter your choice:")

    #ADD STUDENT
    if choice == "1":
        print("\n=====ADD STUDENT=====")
        name=input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        grade = input("Enter Student grade:")

        subjects_input=input("Enter subjects (comma-separated):")
        subjects = subjects_input.split(",")
        student_id = input("Enter Student ID: ")
        dob = input("Enter date of Birth: ")

        #Tuple for student ID and date of Birth
        student_info = (student_id, dob)

        #Add subjects to set
        for subject in subjects:
            subject = subject.strip()
            unique_subjects.add(subject)

        #Dictionary for student information
        student = {
            "student_id" : student_info,
            "name" : name,
            "age": age,
            "grade" : grade,
            "subjects" : subjects
        }

        #Add dictionary to list
        all_students.append(student)

        #dictionary using student ID as key
        student_data[student_id]={
            "name": name,
            "age": age,
            "grade": grade,
            "subjects" : subjects
            }
        print("\nStudent Added Successfully!")

        #f-string formattting
        print(f"Student Name: {name}")
        print(f"Student ID: {student_id}")

    #Display All students
    elif choice == "2":
        print("\n========All Students=======")
        if len(all_students) == 0:
            print("No student records available")
        else:
                for student in all_students:
                    student_id, dob = student["student_id"]
                    print("\n-----------------")
                    print("Student ID: {}". format(student_id))
                    print("Date of Birth: {}". format(dob))
                    print("Student Name: {}" . format(student["name"]))
                    print("Age: {}". format(student["age"]))
                    print("Grade: {}" . format(student["grade"]))
                    print("Subjects: ", end=" ")

                    for subject in student["subjects"]:
                        print(subject, end=" ")
                    print()
                    #formatting
                    print("Student: %s | Grade: %s" %
                          (student["name"],student["grade"]))

                    
    #Update student
    elif choice == "3":
        print("\n==========Update Student=========")
        student_id = input("Enter student id to update:")
        if student_id in student_data:
            print("1. Update age")
            print("2. Update subjects")
            update_choice=input("Enter  your choice:")
            
            if update_choice =="1":
                new_age = int(input("Enter new age:"))

                #update in dictionary
                student_data[student_id]["age"]=new_age

                #update in list
                for student in all_students:
                    if student["student_id"][0]==student_id:
                        student["age"]=new_age
                print("Age Update successfully!")
                
            elif update_choice=="2":
                        new_subjects_input=input("Enter New Subjects(comma-saperated):")
                        new_subjects=new_subjects_input.split(",")

                        #update dictionary
                        student_data[student_id]["subjects"]=new_subjects

                        #update list
                        for student in all_students:
                            if student["student_id"][0]==student_id:
                                student["subjects"]=new_subjects

                        #Add new subject to set
                        for subject in new_subjects:
                            subject=subject.strip()
                            unique_subjects.add(subject)
                        print("Subjects updated successfully")
            else:
                print("Invalid update choice:")
        else:
            print("Student ID not found")
                    
    #delete student
    elif choice =="4":
        print("\n=====Delete student=====")
        student_id = input("Enter student ID to delete:")
        if student_id in student_data:
            for student in all_students:
                if student["student_id"][0]==student_id:
                    index=all_students.index(student)
                    #delete student from main list
                    del all_students[index]
                    break
                
            #delete student from dictionary
            del student_data[student_id]
            print("Student deleetd successfully")
        else:
            print("Student id not found")
            
    #Display Subjects
    elif choice == "5":
        print("\n=====Subject offered====")
        if len(unique_subjects)==0:
            print("No Subjects available")
        else:
            print("Unique Subjects")

            for subject in unique_subjects:
                print(subject)

    #Exit
    elif choice == "6":
        print("\n=======================")
        print("Thank you for using student Data Organizer!")
        print("Program exited successfully!")
        print("============================")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 6")
        
            
        
                
                    
    
