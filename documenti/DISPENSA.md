# Automa meteo in Python: dispensa di laboratorio

**Versione 1.1** — 13/10/2026 — Laboratorio di Informatica, prof. Nicola Regge, Piamarta Milano.

## 00 Che cosa costruisci

Un automa che ogni minuto chiede a un servizio su Internet la temperatura di Milano, la scrive in uno storico (un file che si apre con Excel) e aggiorna una pagina web con il valore, il grafico e la tabella. Alla fine la pagina sarà online e la potrai aprire anche dal telefono.

## 01 Le parole

| Parola | Che cosa vuol dire |
|---|---|
| API REST | un indirizzo web che invece di una pagina restituisce dati (qui: la temperatura) |
| CSV | un file di testo a tabella, con le colonne separate da `;`: si apre con Excel |
| Dashboard | il pannello che mostra lo stato del sistema |
| Commit | un salvataggio del progetto su Git, con una frase che dice che cosa è cambiato |
| GitHub Actions | GitHub che esegue il tuo programma da solo, a orari fissi |
| GitHub Pages | GitHub che pubblica la cartella `docs` come sito web |

## 02 Fase 1: fai girare l'automa su Google Colab

Google Colab è Python nel browser, con il tuo account della scuola: non si installa niente.

1. Apri una scheda nuova e vai su:
```
https://colab.research.google.com
```
2. Clicca «Nuovo blocco note».
3. Nel tuo deposito su GitHub apri il file `automa_meteo.py`, clicca il bottone «Copy raw file» (le due pagine sovrapposte, in alto a destra del codice).
4. Torna su Colab, clicca nella cella grigia e premi Ctrl+V.
5. Clicca il triangolo a sinistra della cella. In basso vedi le letture, una al minuto.
6. Clicca la cartella a sinistra: dentro `docs` trovi `database_temperatura.csv` e `index.html`.
7. Per vedere la dashboard: tre puntini accanto a `index.html`, «Scarica», poi doppio clic sul file scaricato.
8. Per fermare l'automa: il quadrato al posto del triangolo.

**FATTO!** Il tuo automa legge la temperatura vera.

## 03 Fase 2: l'automa sempre acceso, con GitHub

Questa parte gira su GitHub, anche a computer spento.

1. Nel tuo deposito clicca «Actions» in alto. Se chiede di abilitarle, clicca il bottone verde.
2. A sinistra clicca «Automa meteo», poi a destra «Run workflow» e di nuovo «Run workflow».
3. Dopo un minuto compare un pallino verde: l'automa ha fatto la prima lettura e ha salvato lo storico con un commit.
4. Da qui in poi lo fa da solo ogni 30 minuti.

## 04 Fase 3: la dashboard online

1. Nel tuo deposito clicca «Settings», poi a sinistra «Pages».
2. In «Branch» scegli `main` e la cartella `/docs`, poi «Save».
3. Dopo un paio di minuti la dashboard è su:
```
https://chasedeleon.github.io/automa-meteo-python/
```

**FATTO!** Apri il link sul telefono e mostralo.

## 05 Fase 4: ogni miglioria è un commit

1. Cambi qualcosa nel codice su Colab e lo provi.
2. Su GitHub apri `automa_meteo.py`, clicca la matita, premi Ctrl+A e incolla il codice nuovo.
3. Clicca «Commit changes» e scrivi una frase che spiega la modifica, per esempio:
```
v1.2: aggiunta la velocità del vento
```

## 06 Idee per andare avanti

1. Un'altra misura dallo stesso servizio: vento o umidità.
2. Un allarme: se la temperatura supera una soglia, la dashboard diventa rossa.
3. La media della giornata, la minima e la massima.
4. Un'altra città accanto a Milano.

## 07 Registro delle versioni

1. **v1.1 (13/10/2026):** Colab al posto di OnlineGDB (che non lascia uscire i programmi su Internet); ora italiana; virgola nei decimali per Excel; pagina web completa con grafico e tabella; automa sempre acceso con GitHub Actions; dashboard online con GitHub Pages.
2. **v1.0:** prima versione.
