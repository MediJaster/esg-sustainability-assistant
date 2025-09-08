# Guida all'uso

Benvenuto nella guida all'uso del progetto! Questa guida ti fornirà le informazioni necessarie per iniziare a utilizzare il progetto in modo efficace

## Docker (raccomandato)

1. Assicurati di avere Docker installato sulla tua macchina. Puoi scaricarlo da [qui](https://www.docker.com/get-started).
2. Clona il repository:

    ```bash
    git clone https://github.com/MediJaster/esg-sustainability-assistant.git
    ```

3. Naviga nella directory del progetto:

    ```bash
    cd esg-sustainability-assistant
    ```

4. Costruisci e avvia le immagini Docker con Docker Compose:

    ```bash
    docker compose up -d
    ```

Ora potrai accedere al frontend del progetto tramite il tuo browser all'indirizzo [`http://localhost:8501`](http://localhost:8501).

Per accedere direttamente all'interfaccia Swagger di FastAPI, visita [`http://localhost:8080/docs`](http://localhost:8000/docs).

## Sviluppo locale

### Requisiti

-   `uv` e `crewai` installati.

### Installazione

1. Clona il repository:

    ```bash
    git clone https://github.com/MediJaster/esg-sustainability-assistant.git
    ```

2. Naviga nella directory del progetto:

    ```bash
    cd esg-sustainability-assistant
    ```

3. Installa le dipendenze:

    ```bash
    crewai install
    ```

    ```bash
    uv sync --all-groups
    ```

### Configurazione

Configura le variabili d'ambiente necessarie, come le chiavi API per i modelli di linguaggio.

Puoi trovare un esempio di file `.env` nel file `.env.example` nella radice del progetto.

Copia questo file e rinominalo in `.env`, quindi modifica le variabili secondo le tue esigenze.

### Esecuzione

1. Avvia il backend FastAPI:

    ```bash
    uvicorn src.api.main:app --host 0.0.0.0 --port 8080
    ```

2. In un altro terminale, avvia il frontend Streamlit:

    ```bash
    streamlit run src/streamlit_app.py
    ```
