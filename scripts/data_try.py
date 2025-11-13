import requests
import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("EODHD_API_TOKEN")
symbol = "BTC-USD.CC"
#symbol = "SPY.US"

url = f"https://eodhd.com/api/eod/{symbol}?api_token={API_TOKEN}&fmt=json"
#url = f"https://eodhd.com/api/eod/{symbol}?api_token={API_TOKEN}&period=d&fmt=json"

response = requests.get(url)
print("Status:", response.status_code)
print("URL usada:", url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['close'], color='blue', label=symbol)
    plt.title(f'{symbol} - Histórico de precios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio de cierre (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Respuesta del servidor:")
    print(response.text)
