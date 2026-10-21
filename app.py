import sqlite3

# Database connect
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Table create
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT,
    cgpa REAL,
    email TEXT
)
''')
print("Table Ready!")

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    cgpa = float(input("Enter CGPA: "))
    email = input("Enter Email: ")
    cursor.execute("INSERT INTO students VALUES (?,?,?,?,?)", (id, name, branch, cgpa, email))
    conn.commit()
    print("Student Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(row)

def update_cgpa():
    id = int(input("Enter ID to update: "))
    new_cgpa = float(input("Enter New CGPA: "))
    cursor.execute("UPDATE students SET cgpa=? WHERE id=?", (new_cgpa, id))
    conn.commit()
    print("Updated!")

def delete_student():
    id = int(input("Enter ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Deleted!")

while True:
    print("\n1.Add  2.View  3.Update CGPA  4.Delete  5.Exit")
    ch = input("Choose: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        update_cgpa()
    elif ch == '4':
        delete_student()
    elif ch == '5':
        break

conn.close()
