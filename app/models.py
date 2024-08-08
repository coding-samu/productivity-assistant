# Contiene la definizione dei modelli AI e la logica per la prioritizzazione delle attività.

from transformers import pipeline

# Carica un modello preaddestrato per la comprensione del linguaggio
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')

def prioritize_tasks(tasks):
    # Filtra i task vuoti
    valid_tasks = [task for task in tasks if task['task']]
    prioritized = sorted(valid_tasks, key=lambda x: classify_task(x['task']), reverse=True)
    return prioritized

def classify_task(task):
    if not task:
        return 0
    result = classifier(task)[0]
    print(f"Classify Task Result: {result}")  # Aggiungi questa linea per il debug
    return result['score'] if result['label'] == 'POSITIVE' else -result['score']