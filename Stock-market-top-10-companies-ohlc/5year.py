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

# Define the period for the data
start_date = "2019-06-20"
end_date = "2024-06-20"

# Function to fetch OHLC data for a given company over the specified period
def fetch_annual_ohlc_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    ohlc_data = {
        'Open': stock_data['Open'][0],
        'High': stock_data['High'].max(),
        'Low': stock_data['Low'].min(),
        'Close': stock_data['Close'][-1]
    }
    return ohlc_data

# Create a list to store the OHLC data for each company
annual_ohlc_data = []

# Fetch the OHLC data for each company
for company, symbol in companies.items():
    data = fetch_annual_ohlc_data(symbol, start_date, end_date)
    data['Company'] = company
    annual_ohlc_data.append(data)

# Create a DataFrame from the OHLC data
ohlc_df = pd.DataFrame(annual_ohlc_data)

# Reorder columns to have 'Company' first
ohlc_df = ohlc_df[['Company', 'Open', 'High', 'Low', 'Close']]

# Save the OHLC data to an Excel file
ohlc_df.to_excel('5_year_ohlc_data_summary.xlsx', index=False)

print("5-year OHLC data for the specified companies has been saved to '5_year_ohlc_data_summary.xlsx'")
