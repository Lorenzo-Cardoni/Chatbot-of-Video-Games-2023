# rasa-videogame-chatbot

In questa repository presentiamo un chatbot per la raccomandazione dei videogiochi sviluppato utilizzando il framework RASA.

## Requisiti

Per realizzare il progetto abbiamo utilizzato Docker pertanto non sono presenti particolari requisiti, se non l'aver installato docker.
È quindi sufficiente eseguire il comando:

`sudo docker-compose up --build --remove-orphans`

## Struttura della repository

- Assets: contiene file secondari come le copertine dei videogiochi
- Dataset: contiene il dataset nelle sue diverse forme (prima e dopo il processamento)
- Script: contiene script utilizzati in fase di sviluppo
- src: contiene il sorgente che implementa le funzionalità del chatbot sviluppato
