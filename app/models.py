# models.py
from transformers import pipeline
from datetime import datetime, timedelta
from dateutil import parser
import re

# Carica un modello preaddestrato per la comprensione del linguaggio
try:
    classifier = pipeline('text-classification', model='roberta-base')
    print("Classifier loaded successfully.")
except Exception as e:
    print(f"Errore nel caricamento del classificatore: {e}")

def extract_time_info(task):
    """
    Estrae informazioni temporali da un task usando regex e parser.
    """
    time_info = None
    # Prova a estrarre l'informazione temporale usando il parser
    try:
        time_info = parser.parse(task, fuzzy=True)
    except (parser.ParserError, ValueError):
        # Se il parsing fallisce, possiamo lasciare time_info come None
        pass

    return time_info

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
