from user import User

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.submissions = []

    def submit_assignment(self, assignment_id, content):
        # Submits an assignment
        print(f"Assignment {assignment_id} submitted.")
        # You can save submission to a file or DB here