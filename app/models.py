# Contiene la definizione dei modelli AI e la logica per la prioritizzazione delle attività.

from transformers import pipeline

# Carica un modello preaddestrato per la comprensione del linguaggio
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english')

def prioritize_tasks(tasks):
    # Usa l'AI per assegnare priorità in base al contenuto della task
    prioritized = sorted(tasks, key=lambda x: classify_task(x['task']), reverse=True)
    return prioritized

def classify_task(task):
    # Assegna un punteggio di priorità in base all'analisi del testo
    result = classifier(task)[0]
    return result['score'] if result['label'] == 'POSITIVE' else -result['score']
