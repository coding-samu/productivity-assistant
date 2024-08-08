# Punto di ingresso dell'applicazione. Contiene la logica principale del programma e avvia l'assistente.

from flask import Flask, request, jsonify
from app.data.task_manager import TaskManager
from app.models import prioritize_tasks
import os

app = Flask(__name__)

# Inizializza il gestore delle attività
task_manager = TaskManager()

@app.route('/')
def home():
    return "Welcome to the Productivity Assistant!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = task_manager.get_tasks()
    return jsonify(tasks), 200

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    task = data.get('task')
    time_estimate = data.get('time_estimate', 0)
    task_manager.add_task(task, time_estimate)
    return jsonify({"message": "Task added successfully"}), 201

@app.route('/prioritize-tasks', methods=['GET'])
def prioritize_tasks():
    try:
        # Codice per la priorizzazione dei task
        tasks = task_manager.get_tasks()
        prioritized_tasks = sorted(tasks, key=lambda x: x['priority'])
        return jsonify(prioritized_tasks), 200
    except Exception as e:
        # Stampa l'errore per il debug
        print(f"Errore durante la prioritizzazione: {e}")
        return jsonify({"error": "Errore durante la prioritizzazione dei task"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
