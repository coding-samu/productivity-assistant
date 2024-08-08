# Usa una base image Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di progetto
COPY . /app

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Comando di avvio
CMD ["python", "app/main.py"]
