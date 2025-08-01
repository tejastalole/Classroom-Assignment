# 🎓 Classroom Management System

The **Classroom Management System** is a simple and effective tool to manage student assignments, deadlines, submissions, and grading. This system enables streamlined communication between teachers and students, helping both parties stay organized and productive.


## 📌 Project Overview

This project provides a platform where:

- Teachers can create assignments, set deadlines, and grade submissions.

- Students can view, submit, and track their assignments.

- Both roles have access to status reports of assignments — pending, submitted, or graded.


## ✅ Features

### 👨‍🏫 Teacher

- Create new assignments with titles, descriptions, and deadlines

- View list of all submissions for an assignment

- Grade student submissions

- Track submitted and pending assignments


### 👨‍🎓 Student

- View available assignments

- Submit assignments before deadlines

- Check submission status and grades

### 📊 Admin/Reports

- Generate basic reports like:

  - Number of pending assignments

  - Number of submissions per assignment

  - Graded vs ungraded assignments


## 🛠️ Tech Stack

- Language: Python

- Database: SQLite

- UI (Optional): Tkinter / Flask / CLI

- Libraries: ```os```, ```sqlite3```, ```datetime```, etc.


## 🚀 How to Run

1. Clone this repository or download the source code.

```
git clone https://github.com/your-username/classroom-assignment-system.git
cd classroom-assignment-system
```

2. Run the main Python file:

```
python main.py
```

Make sure Python 3.x is installed on your system.


## 🧠 Core Functionalities (Workflow)

1. **Login / Role Selection** – User chooses role (student or teacher).

2. **Teacher Workflow**
    - Create an assignment

    - View and grade submissions

3. Student Workflow

    - View assignment list

    - Submit assignment (file/text)

4. Reports
    
    - Status breakdown: submitted, pending, graded


## 🗃️ Database Structure (Example)

```assignments``` **table:**

| id | title | description | deadline | teacher\_id |
| -- | ----- | ----------- | -------- | ----------- |

```submissions``` **table:**

| id | student_id | assignment_id | content | submitted_on | grade |


## 📈 Future Scope

- Add notifications/reminders for deadlines

- File upload support for assignment submissions

- Web version with Flask/Django

- Role-based authentication system

- Downloadable report generation


## 📄 License

This project is open-source and available under the MIT License.


## 👤 Author

**Tejas Talole**<br>
Developer & Python Enthusiast<br>
[LinkedIn](https://www.linkedin.com/in/tejas-talole/) |
[GitHub](https://github.com/tejastalole)


