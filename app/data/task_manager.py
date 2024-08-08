# Gestisce le operazioni CRUD (Create, Read, Update, Delete) sulle attività e la gestione delle liste di cose da fare.

import json
import os

class TaskManager:
    def __init__(self, file_path='app/data/data_store.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task, time_estimate):
        self.tasks.append({'task': task, 'time_estimate': time_estimate})
        self.save_tasks()

    def get_tasks(self):
        return self.tasks
