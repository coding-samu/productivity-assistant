# Gestisce le operazioni CRUD (Create, Read, Update, Delete) sulle attività e la gestione delle liste di cose da fare.

import json
import os

class TaskManager:
    def __init__(self, file_path='app/data/data_store.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Verifica se il file esiste
        if not os.path.exists(self.file_path):
            return []

        # Prova a caricare i dati dal file
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Se il file è vuoto o malformato, ritorna una lista vuota
            return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task, time_estimate):
        self.tasks.append({'task': task, 'time_estimate': time_estimate})
        self.save_tasks()

    def get_tasks(self):
        return self.tasks
