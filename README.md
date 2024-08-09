# Productivity Assistant

**Productivity Assistant** è un'applicazione web progettata per aiutarti a gestire e prioritizzare le tue attività quotidiane in modo efficiente. Utilizzando modelli di machine learning e tecniche di analisi del linguaggio naturale, l'assistente organizza i tuoi compiti in base alla loro importanza e alle informazioni temporali fornite. L'interfaccia utente intuitiva consente di aggiungere, rimuovere e visualizzare le attività in modo semplice e rapido.

## Funzionalità Principali

- **Aggiunta di Attività:** Inserisci compiti con una stima del tempo necessario per completarli.
- **Prioritizzazione Intelligente:** L'app utilizza modelli di machine learning per ordinare i compiti in modo coerente, considerando tempi e rilevanza.
- **Gestione delle Attività:** Visualizza e gestisci facilmente la lista delle tue attività direttamente dall'interfaccia web.

## Tecnologie Utilizzate

- **Flask:** Framework web per Python.
- **Hugging Face Transformers:** Modelli pre-addestrati per la classificazione dei testi.
- **Docker:** Contenitore per facilitare il deploy dell'applicazione.

## Installazione

1. Clona il repository:
    ```bash
    git clone https://github.com/coding-samu/productivity-assistant.git
    ```
2. Avvia l'applicazione:
    ```bash
    docker-compose up --build
    ```

## Utilizzo

Accedi all'applicazione visitando `http://localhost:8000` nel tuo browser. Da qui, puoi iniziare a gestire e prioritizzare le tue attività.
