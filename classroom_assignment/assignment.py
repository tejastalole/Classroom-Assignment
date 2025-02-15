# assignment.py
class Assignment:
    def __init__(self, assignment_id, title, description, deadline, max_score):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.max_score = max_score

    def __str__(self):
        return f"Assignment {self.assignment_id}: {self.title} (Max Score: {self.max_score})"
