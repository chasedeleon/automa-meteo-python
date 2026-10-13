# Il percorso del tuo primo progetto

**Versione 1.1** — 13/10/2026 — Laboratorio di Informatica, prof. Nicola Regge, Piamarta Milano.

Dieci tappe, una alla volta. Ogni tappa ha un obiettivo, i passi, il momento in cui è **FATTA**, il commit da fare e una domanda: se sai rispondere a voce, con parole tue, la tappa è davvero tua.

Le domande si fanno nella chat del progetto, cioè nei commenti della Pull Request o di una Issue sul tuo deposito. Il prof e Claude rispondono lì.

**La tua chat di Claude (claude.ai, gratuita):** usala per farti spiegare il codice e gli errori, non per farti scrivere le tappe. La regola è una: quello che metti nel deposito lo devi saper spiegare a voce, con parole tue. Quella chat non è collegata al progetto: quello che il prof deve vedere scrivilo nei commenti su GitHub.

| Tappa | Obiettivo | Stato |
|---|---|---|
| 0 | Account GitHub e deposito | fatta il 13/10/2026 |
| 1 | La prima Pull Request accettata | fatta il 13/10/2026 |
| 2 | L'automa gira su Colab | da fare |
| 3 | Capire il codice | da fare |
| 4 | L'automa sempre acceso | fatta il 13/10/2026 |
| 5 | La dashboard online | fatta il 13/10/2026 |
| 6 | Fallo tuo | da fare |
| 7 | Una misura nuova | da fare |
| 8 | L'allarme | da fare |
| 9 | Le statistiche | da fare |
| 10 | La versione 2.0 e la presentazione | da fare |

## Tappa 1: la prima Pull Request accettata

1. **Obiettivo:** portare la v1.1 nel tuo deposito.
2. **Passi:** apri la Pull Request n. 1, leggi «Files changed», scrivi una domanda nei commenti se qualcosa non è chiaro, poi clicca «Merge pull request» e «Confirm merge».
3. **FATTA quando** nel tuo deposito vedi le cartelle `docs`, `documenti` e `storia`.
4. **Sai spiegarlo?** Che cos'è una Pull Request e perché in un'azienda non si scrive direttamente sul progetto degli altri?

## Tappa 2: l'automa gira su Colab

1. **Obiettivo:** vedere la temperatura vera scorrere sullo schermo.
2. **Passi:** dispensa, capitolo 02.
3. **FATTA quando** vedi almeno tre letture e il file `database_temperatura.csv` si apre in Excel con i numeri giusti.
4. **Sai spiegarlo?** Che cos'è un'API REST? Che cosa succede se Internet non risponde?

## Tappa 3: capire il codice

1. **Obiettivo:** sapere che cosa fa ogni funzione.
2. **Passi:** per ognuna delle cinque funzioni (`leggi_temperatura_api`, `salva_nel_database`, `leggi_storico`, `genera_dashboard`, `una_lettura`) scrivi in `storia/` una riga con parole tue: che cosa riceve, che cosa fa, che cosa restituisce.
3. **FATTA quando** il file è nel deposito con un commit.
4. **Commit:**
```
Tappa 3: le funzioni spiegate con parole mie
```
5. **Sai spiegarlo?** Perché la temperatura si salva con la virgola e non con il punto?

## Tappa 4: l'automa sempre acceso

1. **Obiettivo:** l'automa lavora da solo, ogni 30 minuti, a computer spento.
2. **Passi:** dispensa, capitolo 03.
3. **FATTA quando** in «Actions» vedi il pallino verde e nella cronologia dei commit compaiono le «Lettura automatica».
4. **Sai spiegarlo?** Che differenza c'è tra il ciclo `while True` su Colab e il lavoro di GitHub Actions?

## Tappa 5: la dashboard online

1. **Obiettivo:** il tuo pannello è su Internet.
2. **Passi:** dispensa, capitolo 04.
3. **FATTA quando** apri il link dal telefono e lo mostri a qualcuno.
4. **Sai spiegarlo?** Perché il deposito deve essere pubblico per usare GitHub Pages?

## Tappa 6: fallo tuo

1. **Obiettivo:** il progetto diventa tuo.
2. **Passi:** scegli tu: il nome della stazione, i colori della dashboard, un'altra città (cambia `LATITUDINE` e `LONGITUDINE`), un logo.
3. **FATTA quando** la dashboard online mostra la tua scelta.
4. **Commit:**
```
Tappa 6: la mia stazione
```

## Tappa 7: una misura nuova

1. **Obiettivo:** la tua prima modifica vera al codice.
2. **Passi:** il servizio dà anche il vento (`windspeed`). Aggiungilo allo storico (una colonna in più) e alla dashboard. Prova su Colab, poi il commit.
3. **FATTA quando** la dashboard mostra temperatura e vento.
4. **Commit:**
```
v1.2: aggiunta la velocità del vento
```
5. **Sai spiegarlo?** Che cosa hai cambiato in ognuna delle funzioni?

## Tappa 8: l'allarme

1. **Obiettivo:** come in un vero sistema di controllo, un allarme.
2. **Passi:** scegli una soglia (per esempio 25 °C). Se la temperatura la supera, la dashboard diventa rossa e scrive «ALLARME».
3. **FATTA quando** provi con una soglia bassa e vedi la dashboard rossa.
4. **Commit:**
```
v1.3: allarme di temperatura
```

## Tappa 9: le statistiche

1. **Obiettivo:** leggere i dati, non solo raccoglierli.
2. **Passi:** sulla dashboard la minima, la massima e la media della giornata.
3. **FATTA quando** i numeri della dashboard coincidono con quelli che calcoli in Excel sullo storico.
4. **Commit:**
```
v1.4: minima, massima e media del giorno
```

## Tappa 10: la versione 2.0 e la presentazione

1. **Obiettivo:** chiudere il progetto come in un'azienda.
2. **Passi:** su GitHub crei una Release `v2.0` con l'elenco delle novità; prepari cinque minuti di presentazione: il problema, l'architettura (i quattro blocchi), una demo dal telefono, che cosa hai imparato.
3. **FATTA quando** presenti al prof e alla classe.
4. **Sai spiegarlo?** Come assomiglia il tuo automa a un sistema di controllo industriale come EPICS?

## Registro delle versioni

1. **v1.1 (13/10/2026):** come usare la chat gratuita di Claude.
2. **v1.0 (13/10/2026):** prima versione del percorso.
