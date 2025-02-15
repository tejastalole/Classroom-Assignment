# db_manager.py
import sqlite3

class DBManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS submissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    assignment_id INTEGER,
                    student_id INTEGER,
                    content TEXT,
                    grade INTEGER DEFAULT NULL
                );
            """)
    
    def save_submission(self, assignment_id, student_id, content):
        with self.conn:
            self.conn.execute("""
                INSERT INTO submissions (assignment_id, student_id, content)
                VALUES (?, ?, ?)
            """, (assignment_id, student_id, content))
    
    def get_submissions(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM submissions WHERE student_id = ?
        """, (student_id,))
        return cursor.fetchall()
