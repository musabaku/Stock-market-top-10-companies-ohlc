import yfinance as yf
import pandas as pd

# Define the list of companies and their stock symbols
companies = {
    "Koç Holding": "KCHOL.IS",
    "Turkish Airlines": "THYAO.IS",
    "BIM": "BIMAS.IS",
    "Şişecam": "SISE.IS",
    "Vestel": "VESTL.IS",
    "Arçelik": "ARCLK.IS",
    "Aselsan": "ASELS.IS",
    "Bayraktar": "BAYRK.IS",  # Assuming this is the correct symbol, please verify
    "Turkcell": "TCELL.IS",
    "Türk Telekom": "TTKOM.IS",
    "Emlak Konut": "EKGYO.IS",
    "Ford Otosan": "FROTO.IS",
    "Enka": "ENKAI.IS"
}

# Define the period and interval for the data
period = "1y"
interval = "1d"

# Function to fetch OHLC data for a given company over the year
def fetch_annual_ohlc_data(symbol):
    stock_data = yf.download(symbol, period=period, interval=interval)
    ohlc_data = {
        'Open': stock_data['Open'][0],
        'High': stock_data['High'].max(),
        'Low': stock_data['Low'].min(),
        'Close': stock_data['Close'][-1]
    }
    return ohlc_data

# Create a list to store the annual OHLC data for each company
annual_ohlc_data = []

# Fetch the annual OHLC data for each company
for company, symbol in companies.items():
    data = fetch_annual_ohlc_data(symbol)
    data['Company'] = company
    annual_ohlc_data.append(data)

# Create a DataFrame from the annual OHLC data
ohlc_df = pd.DataFrame(annual_ohlc_data)

# Reorder columns to have 'Company' first
ohlc_df = ohlc_df[['Company', 'Open', 'High', 'Low', 'Close']]

# Save the OHLC data to an Excel file
ohlc_df.to_excel('annual_ohlc_data.xlsx', index=False)

print("Annual OHLC data for the specified companies has been saved to 'annual_ohlc_data.xlsx'")
