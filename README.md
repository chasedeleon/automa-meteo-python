# automa-meteo-python

Progetto di stage: un **automa** in Python che legge la temperatura vera di Milano da Internet, la salva in uno **storico** e la mostra in una **dashboard** web. Simula, in piccolo, un sistema di controllo industriale (come EPICS): sorgente dei dati, automa, database storico, pannello di controllo.

## Come è fatto

| Pezzo | Che cosa fa | File |
|---|---|---|
| Sorgente dati | il servizio pubblico Open-Meteo (API REST) dà la temperatura attuale | — |
| Automa | legge la misura, la salva, aggiorna la dashboard | `automa_meteo.py` |
| Storico | tutte le letture, si apre con Excel | `docs/database_temperatura.csv` |
| Dashboard | ultima temperatura, grafico, tabella | `docs/index.html` |
| Automa sempre acceso | GitHub esegue una lettura ogni 30 minuti, senza nessun PC | `.github/workflows/automa.yml` |

## Dove si vede

Quando GitHub Pages è attivo, la dashboard è su `https://chasedeleon.github.io/automa-meteo-python/` (anche dal telefono).

## Versioni

1. **v1.1** — ora italiana, virgola nei decimali per Excel, pagina web completa con grafico e tabella, automa sempre acceso con GitHub Actions, dashboard su GitHub Pages, lavoro in laboratorio su Google Colab.
2. **v1.0** — prima versione della dispensa: lettura, storico CSV, dashboard in un file.
