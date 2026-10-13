import urllib.request
import json
import time

# URL dell'API REST pubblica per la temperatura reale (Coordinate di Milano)
URL_API = "https://api.open-meteo.com/v1/forecast?latitude=45.4642&longitude=9.1900&current_weather=true"

FILE_DATABASE = "database_temperatura.csv"
FILE_DASHBOARD = "dashboard.html"

def leggi_temperatura_api():
    """Connessione all'API REST e lettura della temperatura reale."""
    try:
        req = urllib.request.Request(URL_API, headers={'User-Agent': 'Python-School-App'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            temp = data["current_weather"]["temperature"]
            return temp
    except Exception as e:
        print(f"Errore durante il recupero del dato: {e}")
        return None

def salva_nel_database(ora, data, temp):
    """Registrazione del dato nel file CSV (compatibile con Excel)."""
    try:
        with open(FILE_DATABASE, "x") as f:
            f.write("Data;Ora;Temperatura_C\n")
    except FileExistsError:
        pass

    with open(FILE_DATABASE, "a") as f:
        f.write(f"{data};{ora};{temp}\n")

def genera_dashboard(ora, data, temp):
    """Generazione dell'interfaccia grafica web HTML."""
    html_content = f"""


    <meta http-equiv="refresh" content="10">
    <title>Pannello Monitoraggio Temperatura</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1e1e2e;
            color: #cdd6f4;
            text-align: center;
            padding-top: 40px;
        }}
        .card {{
            background-color: #313244;
            display: inline-block;
            padding: 30px 50px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            border: 2px solid #45475a;
        }}
        .valore {{
            font-size: 64px;
            font-weight: bold;
            color: #89b4fa;
            margin: 20px 0;
        }}
        .status {{
            color: #a6e3a1;
            font-size: 14px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h2>STAZIONE METEO - MONITORAGGIO REALE</h2>
        <p>Ultimo Aggiornamento: <b>{data}</b> alle <b>{ora}</b></p>
        <div class="valore">{temp} °C</div>
        <p class="status">● Automa attivo - Connessione API REST OK</p>
        <p><small>Dati salvati in continuo nel database: <i>{FILE_DATABASE}</i></small></p>
    </div>
</body>
</html>"""

    with open(FILE_DASHBOARD, "w", encoding="utf-8") as f:
        f.write(html_content)

# --- CICLO DI ESECUZIONE CONTINUA ---
print("🚀 Automa avviato su OnlineGDB!")

while True:
    ora_attuale = time.strftime("%H:%M:%S")
    data_attuale = time.strftime("%d/%m/%Y")
    
    print(f"\n[{ora_attuale}] Interrogazione API REST in corso...")
    temperatura = leggi_temperatura_api()
    
    if temperatura is not None:
        print(f"-> Temperatura attuale: {temperatura} °C")
        salva_nel_database(ora_attuale, data_attuale, temperatura)
        print(f"-> Misurazione registrata su '{FILE_DATABASE}'")
        genera_dashboard(ora_attuale, data_attuale, temperatura)
        print(f"-> Dashboard '{FILE_DASHBOARD}' aggiornata!")
    else:
        print("-> Impossibile recuperare il dato dall'API.")
        
    # Attesa di 60 secondi prima del prossimo ciclo
    time.sleep(60)