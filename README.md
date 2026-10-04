🎓 Student Data Organizer
> 🐍 A beginner-friendly Python project for managing student records using **List, Tuple, Set, and Dictionary**.
---
🌟 Project Overview
Student Data Organizer is a menu-driven Python program that manages student records.
With this project, you can:
➕ Add student records
📋 Display all students
✏️ Update student information
🗑️ Delete student records
📚 Display unique subjects offered
🚪 Exit the program safely
The project demonstrates important Python collection concepts such as List, Tuple, Set, and Dictionary, along with string formatting, type casting, mutability/immutability, and the `del` keyword.
---
🎯 Project Objective
The main objective of this project is to understand how different Python collection data types can work together to organize and manage student information.
Concepts Used
Concept	Used For
📋 List	Storing multiple student records
🔒 Tuple	Storing Student ID and Date of Birth
🔵 Set	Storing unique subjects without duplicates
📖 Dictionary	Storing student information using Student ID
🔄 Type Casting	Converting age input into an integer
✂️ String Manipulation	Splitting and cleaning subject input
📝 String Formatting	f-string, `.format()`, and `%` formatting
🗑️ del keyword	Removing student records
🔁 while loop	Keeping the menu running
---
🧩 Main Menu
```text
==========MENU==========
1. Add Student
2. Display All student
3. Update Student Information
4. Delete Student
5. Display Student Subject Offered
6. Exit
==========================
```
---
⚙️ Features
1️⃣ Add Student
The program accepts:
👤 Student Name
🎂 Age
🎓 Grade
📚 Subjects
🆔 Student ID
📅 Date of Birth
The information is stored using different collection types.
2️⃣ Display All Students
Displays the saved student records with:
Student ID
Date of Birth
Name
Age
Grade
Subjects
3️⃣ Update Student Information
The program allows updating:
🎂 Student age
📚 Student subjects
4️⃣ Delete Student
A student can be removed using their Student ID.
5️⃣ Display Unique Subjects
The program displays subjects stored in a set, so duplicate subjects are not stored multiple times.
6️⃣ Exit
The program displays a thank-you message and exits successfully.
---
🗂️ Project Structure
```text
Student_Data_Organizer/
│
├── Collection_manipulator.py
├── README.md
│
└── screenshots/
    ├── Screenshot_01.png
    ├── Screenshot_02.png
    ├── Screenshot_03.png
    ├── Screenshot_04.png
    ├── Screenshot_05.png
    └── Screenshot_06.png
```
> 🎥 The project demonstration video can also be added to the GitHub repository separately.
---
📸 Project Screenshots
🖥️ Screenshot 1
![Student Data Organizer - Screenshot 1](screenshots/Screenshot_01.png)
🖥️ Screenshot 2
![Student Data Organizer - Screenshot 2](screenshots/Screenshot_02.png)
🖥️ Screenshot 3
![Student Data Organizer - Screenshot 3](screenshots/Screenshot_03.png)
🖥️ Screenshot 4
![Student Data Organizer - Screenshot 4](screenshots/Screenshot_04.png)
🖥️ Screenshot 5
![Student Data Organizer - Screenshot 5](screenshots/Screenshot_05.png)
🖥️ Screenshot 6
![Student Data Organizer - Screenshot 6](screenshots/Screenshot_06.png)
---
🧠 How the Collections Are Used
📋 List
```python
all_students = []
```
The list stores multiple student records.
🔒 Tuple
```python
student_info = (student_id, dob)
```
The tuple stores Student ID and Date of Birth together.
🔵 Set
```python
unique_subjects = set()
```
The set stores unique subjects and prevents duplicate values.
📖 Dictionary
```python
student_data = {}
```
The dictionary uses Student ID as the key and stores the student's information as the value.
---
📝 String Formatting
This project demonstrates three styles of string formatting.
f-string
```python
print(f"Student Name: {name}")
```
`.format()`
```python
print("Student Name: {}".format(student["name"]))
```
`%` formatting
```python
print("Student: %s | Grade: %s" %
      (student["name"], student["grade"]))
```
---
🔄 Program Flow
```text
Start
  ↓
Display Menu
  ↓
Choose an Option
  ↓
┌─────────────────────────────┐
│ 1. Add Student              │
│ 2. Display Students         │
│ 3. Update Information       │
│ 4. Delete Student           │
│ 5. Display Unique Subjects  │
│ 6. Exit                     │
└─────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Menu
  ↓
Exit
```
---
💻 Requirements
🐍 Python 3.x
Any Python IDE, such as:
IDLE
VS Code
PyCharm
No external Python libraries are required.
---
▶️ How to Run
Download or clone this repository.
Open `Collection_manipulator.py`.
Run the Python file.
Select an option from the menu.
Enter the requested student information.
Example:
```text
Enter your choice: 1

=====ADD STUDENT=====
Enter Student Name: Rahul
Enter Student Age: 20
Enter Student grade: A
Enter subjects (comma-separated): Python,Math,English
Enter Student ID: S101
Enter date of Birth: 01-01-2006

Student Added Successfully!
```
---
📚 Learning Outcomes
After completing this project, the following Python concepts can be practiced:
✅ Working with collections  
✅ Managing multiple records  
✅ List mutability  
✅ Tuple immutability  
✅ Removing duplicates using sets  
✅ Dictionary key-value storage  
✅ Type casting with `int()`  
✅ String splitting with `.split()`  
✅ String formatting  
✅ Updating and deleting data  
✅ Menu-driven programming  
✅ Using loops and conditional statements
---
🎥 Project Demonstration
A demonstration video was recorded for this project.
Video file: `2026-10-04 02-13-16.mp4`
> 📌 GitHub does not normally display an MP4 directly inside a README when it is stored like an ordinary image. Upload the video to the repository and link it separately, or attach it to a GitHub issue/release if you want an easy browser-playable link.
---
👩‍💻 Project Information
Project Name: Collection Manipulator  
Program Name: Student Data Organizer  
Language: Python 🐍  
Project Type: Console-based application  
Level: Beginner / Intermediate
---
⭐ Thank You!
Thank you for checking out the Student Data Organizer! 🎓🐍
This project was created to practice Python collection data types and basic data management concepts.
Happy Coding! 💻✨
