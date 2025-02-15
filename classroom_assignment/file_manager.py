# file_manager.py
import json

class FileManager:
    @staticmethod
    def load_users():
        try:
            with open("data/users.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_users(file_path, users_data):
        with open("data/users.json", 'w') as file:
            json.dump(users_data, file)
