contacts = { 
    'number': 4,
    'students': 
        [
            { 'name': 'Alice', 'age': 20, 'grade': 'A', 'email':'alice@gmail.com' },
            { 'name': 'Bob', 'age': 22, 'grade': 'B', 'email':'bob@gmail.com' },
            { 'name': 'Charlie', 'age': 23, 'grade': 'C', 'email':'charlie@gmail.com' },
            { 'name': 'David', 'age': 21, 'grade': 'D', 'email':'david@gmail.com' }
        ]
}

print("Student Contacts")
for student in contacts['students']:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Email: {student['email']}")  