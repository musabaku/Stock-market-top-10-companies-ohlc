import yfinance as yf
import pandas as pd

# Define the list of companies and their stock symbols
companies = {
    "Koç Holding": "KCHOL.IS",
    "Ereğli Demir ve Çelik Fabrikaları": "EREGL.IS",
    "Turkish Airlines": "THYAO.IS",
    "Akbank": "AKBNK.IS",
    "Aselsan": "ASELS.IS",
    "Arçelik": "ARCLK.IS",
    "Şişecam": "SISE.IS",
    "Tüpraş": "TUPRS.IS",
    "Garanti Bank": "GARAN.IS",
    "Yapı ve Kredi Bankası": "YKBNK.IS"
}

# Define the period and interval for the data
period = "1y"
interval = "1d"

# Function to fetch OHLC data for a given company
def fetch_ohlc_data(symbol):
    stock_data = yf.download(symbol, period=period, interval=interval)
    return stock_data[['Open', 'High', 'Low', 'Close']]

# Create a dictionary to store the OHLC data for each company
ohlc_data = {}

# Fetch the OHLC data for each company
for company, symbol in companies.items():
    ohlc_data[company] = fetch_ohlc_data(symbol)

# Save the OHLC data to an Excel file
with pd.ExcelWriter('ohlc_data.xlsx') as writer:
    for company, data in ohlc_data.items():
        data.to_excel(writer, sheet_name=company)

print("OHLC data for the specified companies has been saved to 'ohlc_data.xlsx'")
