# main.py
from flask import Flask, render_template, request, jsonify
from app.data.task_manager import TaskManager
from app.models import prioritize_tasks_model  # Cambia il nome dell'import

app = Flask(__name__)

# Inizializza il gestore delle attività
task_manager = TaskManager()

@app.route('/')
def home():
    return render_template('index.html')  # Renderizza il file HTML nella cartella templates

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
def prioritize_tasks_route():  # Cambia il nome della funzione di Flask
    try:
        tasks = task_manager.get_tasks()
        prioritized_tasks = prioritize_tasks_model(tasks)  # Chiama la funzione con il nuovo nome
        return jsonify(prioritized_tasks), 200
    except Exception as e:
        # Stampa l'errore per il debug
        print(f"Errore durante la prioritizzazione: {e}")
        return jsonify({"error": "Errore durante la prioritizzazione dei task"}), 500

@app.route('/remove-task', methods=['POST'])
def remove_task():
    try:
        data = request.json
        task_name = data.get('task')
        task_manager.remove_task(task_name)
        return jsonify({"message": "Task removed successfully"}), 200
    except Exception as e:
        print(f"Errore durante la rimozione del task: {e}")
        return jsonify({"error": "Errore durante la rimozione del task"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
