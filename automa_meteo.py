"""AUTOMA METEO - versione 1.1

Legge la temperatura vera di Milano da un servizio pubblico su Internet (API REST Open-Meteo),
la salva in uno storico (file CSV che si apre con Excel) e costruisce una pagina web con
l'ultimo valore, il grafico e la tabella delle ultime letture (la dashboard).

Due modi di farlo girare:
  python automa_meteo.py              -> gira sempre, una lettura ogni 60 secondi (in laboratorio, su Google Colab)
  python automa_meteo.py --una-volta  -> fa una sola lettura e si ferma (lo usa GitHub Actions ogni 30 minuti)
"""
import json
import sys
import time
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

# Coordinate di Milano. Per un'altra città basta cambiare questi due numeri.
LATITUDINE = 45.4642
LONGITUDINE = 9.1900
URL_API = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={LATITUDINE}&longitude={LONGITUDINE}&current_weather=true")

FILE_DATABASE = "docs/database_temperatura.csv"
FILE_DASHBOARD = "docs/index.html"
FUSO = ZoneInfo("Europe/Rome")   # ora italiana, anche se il computer che esegue è altrove
OGNI_SECONDI = 60
ULTIME_IN_TABELLA = 20


def leggi_temperatura_api():
    """Chiede la temperatura al servizio Open-Meteo. Restituisce un numero, oppure None se non risponde."""
    try:
        richiesta = urllib.request.Request(URL_API, headers={"User-Agent": "Automa-Meteo-Scuola"})
        with urllib.request.urlopen(richiesta, timeout=20) as risposta:
            dati = json.loads(risposta.read().decode())
            return float(dati["current_weather"]["temperature"])
    except Exception as errore:
        print(f"Errore durante il recupero del dato: {errore}")
        return None


def salva_nel_database(data, ora, temperatura):
    """Aggiunge una riga allo storico. Separatore ';' e virgola nei decimali: Excel in italiano li legge come numeri."""
    try:
        with open(FILE_DATABASE, "x", encoding="utf-8") as f:
            f.write("Data;Ora;Temperatura_C\n")
    except FileExistsError:
        pass
    with open(FILE_DATABASE, "a", encoding="utf-8") as f:
        f.write(f"{data};{ora};{str(temperatura).replace('.', ',')}\n")


def leggi_storico():
    """Legge lo storico e restituisce una lista di (data, ora, temperatura)."""
    righe = []
    try:
        with open(FILE_DATABASE, encoding="utf-8") as f:
            for riga in f.read().splitlines()[1:]:
                parti = riga.split(";")
                if len(parti) == 3:
                    righe.append((parti[0], parti[1], float(parti[2].replace(",", "."))))
    except FileNotFoundError:
        pass
    return righe


def grafico_svg(valori):
    """Disegna il grafico delle temperature come immagine SVG (una linea), senza librerie."""
    if len(valori) < 2:
        return "<p>Il grafico compare dalla seconda lettura.</p>"
    larghezza, altezza, margine = 600, 200, 30
    minimo, massimo = min(valori), max(valori)
    if massimo == minimo:
        massimo = minimo + 1
    punti = []
    for i, v in enumerate(valori):
        x = margine + i * (larghezza - 2 * margine) / (len(valori) - 1)
        y = altezza - margine - (v - minimo) * (altezza - 2 * margine) / (massimo - minimo)
        punti.append(f"{x:.1f},{y:.1f}")
    return (f'<svg viewBox="0 0 {larghezza} {altezza}" role="img" aria-label="Grafico delle temperature">'
            f'<text x="4" y="{margine}" class="asse">{massimo:.1f}°</text>'
            f'<text x="4" y="{altezza - margine}" class="asse">{minimo:.1f}°</text>'
            f'<polyline fill="none" stroke="#89b4fa" stroke-width="3" points="{" ".join(punti)}"/></svg>')


def genera_dashboard():
    """Scrive la pagina web con l'ultima lettura, il grafico e la tabella delle ultime letture."""
    storico = leggi_storico()
    if not storico:
        return
    data, ora, temperatura = storico[-1]
    ultime = storico[-ULTIME_IN_TABELLA:]
    righe_tabella = "".join(
        f"<tr><td>{d}</td><td>{o}</td><td>{str(t).replace('.', ',')} °C</td></tr>" for d, o, t in reversed(ultime))
    pagina = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="60">
<title>Stazione meteo - Milano</title>
<style>
  body {{ font-family: 'Segoe UI', Tahoma, Arial, sans-serif; background: #1e1e2e; color: #cdd6f4; text-align: center; padding: 30px 16px; }}
  .card {{ background: #313244; display: inline-block; padding: 24px 40px; border-radius: 16px; border: 2px solid #45475a; max-width: 680px; width: 100%; box-sizing: border-box; }}
  .valore {{ font-size: 64px; font-weight: bold; color: #89b4fa; margin: 12px 0; }}
  .status {{ color: #a6e3a1; font-size: 14px; font-weight: bold; }}
  svg {{ width: 100%; height: auto; margin: 10px 0; }}
  .asse {{ fill: #a6adc8; font-size: 12px; }}
  table {{ margin: 10px auto; border-collapse: collapse; }}
  td, th {{ padding: 4px 14px; border-bottom: 1px solid #45475a; }}
  a {{ color: #89b4fa; }}
</style>
</head>
<body>
<div class="card">
  <h2>STAZIONE PIAMARTA - MILANO</h2>
  <p>Ultima lettura: <b>{data}</b> alle <b>{ora}</b></p>
  <div class="valore">{str(temperatura).replace('.', ',')} °C</div>
  <p class="status">● Automa attivo - dati dal servizio Open-Meteo</p>
  {grafico_svg([t for _, _, t in ultime])}
  <table><tr><th>Data</th><th>Ora</th><th>Temperatura</th></tr>{righe_tabella}</table>
  <p><small>Letture salvate: {len(storico)} · <a href="database_temperatura.csv">scarica lo storico (CSV per Excel)</a></small></p>
</div>
</body>
</html>
"""
    with open(FILE_DASHBOARD, "w", encoding="utf-8") as f:
        f.write(pagina)


def una_lettura():
    adesso = datetime.now(FUSO)
    data, ora = adesso.strftime("%d/%m/%Y"), adesso.strftime("%H:%M:%S")
    print(f"\n[{ora}] Interrogazione API REST in corso...")
    temperatura = leggi_temperatura_api()
    if temperatura is None:
        print("-> Impossibile recuperare il dato dall'API.")
        return False
    print(f"-> Temperatura attuale: {temperatura} °C")
    salva_nel_database(data, ora, temperatura)
    print(f"-> Misurazione registrata su '{FILE_DATABASE}'")
    genera_dashboard()
    print(f"-> Dashboard '{FILE_DASHBOARD}' aggiornata!")
    return True


if __name__ == "__main__":
    import os
    os.makedirs("docs", exist_ok=True)
    if "--una-volta" in sys.argv:
        sys.exit(0 if una_lettura() else 1)
    print("Automa avviato! Per fermarlo: il bottone Stop (quadrato) in alto.")
    while True:
        una_lettura()
        time.sleep(OGNI_SECONDI)
