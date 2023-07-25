import yfinance as yf
import ta
import matplotlib.pyplot as plt

# Function to calculate and plot RSI and MACD
def analyze_rsi_macd(stock_symbol, start_date, end_date):
    # Fetch historical data from Yahoo Finance
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate RSI
    rsi = ta.momentum.RSIIndicator(data['Close'])
    data['RSI'] = rsi.rsi()

    # Calculate MACD
    macd = ta.trend.MACD(data['Close'])
    data['MACD'] = macd.macd()
    data['Signal_Line'] = macd.macd_signal()

    # Plot RSI and MACD
    plt.figure(figsize=(12, 6))

    # Plot RSI
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['RSI'], label='RSI')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title(f'{stock_symbol} RSI')
    plt.legend()

    # Plot MACD
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['MACD'], label='MACD')
    plt.plot(data.index, data['Signal_Line'], label='Signal Line')
    plt.title(f'{stock_symbol} MACD')
    plt.legend()

    plt.show()

# Example: Analyze RSI and MACD for Apple (AAPL) stock from 2022-01-01 to 2022-07-31
stock_symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2022-07-31'
analyze_rsi_macd(stock_symbol, start_date, end_date)
