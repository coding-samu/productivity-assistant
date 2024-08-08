# Usa una base image Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di progetto
COPY . /app

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta 8000 per Flask
EXPOSE 8000

# Comando di avvio
CMD ["python", "-m", "app.main"]
