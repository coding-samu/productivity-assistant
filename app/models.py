# models.py
from transformers import pipeline

# Carica un modello preaddestrato per la comprensione del linguaggio
try:
    classifier = pipeline('text-classification', model='roberta-base')
    print("Classifier loaded successfully.")
except Exception as e:
    print(f"Errore nel caricamento del classificatore: {e}")

def prioritize_tasks_model(tasks):
    valid_tasks = [task for task in tasks if task.get('task')]
    prioritized = sorted(valid_tasks, key=lambda x: classify_task(x['task']), reverse=True)
    return prioritized

def classify_task(task):
    if not task:
        return 0  # Priorità neutra per task vuoti o nulli
    try:
        result = classifier(task)[0]
        return result['score'] if result['label'] == 'POSITIVE' else -result['score']
    except Exception as e:
        print(f"Errore nella classificazione del task: {e}")
        return 0  # Se c'è un errore nella classificazione, assegna priorità neutra
