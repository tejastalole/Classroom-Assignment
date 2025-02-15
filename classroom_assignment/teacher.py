from user import User

class Teacher(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def create_assignment(self, title, description, deadline, max_score):
        print(f"Assignment '{title}' created.")
        # Save assignment details to file or DB