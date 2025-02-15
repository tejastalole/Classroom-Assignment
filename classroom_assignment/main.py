# main.py
from student import Student
from teacher import Teacher
from assignment import Assignment
from db_manager import DBManager
from file_manager import FileManager

# Load users from file
users_file = 'data/users.json'
users_data = FileManager.load_users()

# Initialize DB
db = DBManager('classroom.db')

# Creating Teacher and Student objects
teacher = Teacher(user_id=1, name="John Doe")
student = Student(user_id=101, name="Jane Smith")

# Teacher creates an assignment
assignment = Assignment(assignment_id=1, title="Math Homework", description="Algebra", deadline="2024-09-15", max_score=100)
teacher.create_assignment(assignment.title, assignment.description, assignment.deadline, assignment.max_score)

# Student submits an assignment
student.submit_assignment(assignment_id=1, content="Solution to Algebra")

# Save users back to file
FileManager.save_users(users_file, users_data)
