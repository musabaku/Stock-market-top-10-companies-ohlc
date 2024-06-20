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

# Compare the fetched data with the provided data
provided_data = {
    'Company': ["Koç Holding", "Turkish Airlines", "BIM", "Şişecam", "Vestel", "Arçelik", "Aselsan", "Bayraktar", "Turkcell", "Türk Telekom", "Emlak Konut", "Ford Otosan", "Enka"],
    'Open': [95.05, 173.5, 172, 40.26, 45.42, 106.1, 24.65, 4.49, 34.02, 18.47, 6.77, 657, 26.46],
    'High': [270.75, 332, 572.5, 57.45, 107.3, 196.1, 67.3, 80.3, 107.1, 52, 12.03, 1249, 42.74],
    'Low': [93.95, 168.1, 157.1, 39.26, 42.54, 104.8, 24.16, 4.38, 33.1, 17.48, 6.28, 651.4, 25.9],
    'Close': [222.8, 311.5, 563, 48.94, 87.95, 175.1, 60.25, 63.75, 100.9, 51.4, 9, 1087, 41.9]
}

provided_df = pd.DataFrame(provided_data)

comparison_df = pd.merge(ohlc_df, provided_df, on='Company', suffixes=('_fetched', '_provided'))
comparison_df['Open_diff'] = comparison_df['Open_fetched'] - comparison_df['Open_provided']
comparison_df['High_diff'] = comparison_df['High_fetched'] - comparison_df['High_provided']
comparison_df['Low_diff'] = comparison_df['Low_fetched'] - comparison_df['Low_provided']
comparison_df['Close_diff'] = comparison_df['Close_fetched'] - comparison_df['Close_provided']

# Display the differences
print(comparison_df[['Company', 'Open_diff', 'High_diff', 'Low_diff', 'Close_diff']])
