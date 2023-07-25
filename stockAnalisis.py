import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import ta

# Fungsi untuk melakukan analisis teknikal dan menggambar chart
def technical_analysis(stock_symbol, start_date, end_date):
    # Mengambil data saham dari Yahoo Finance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Menghitung moving average (10, 20, 50, 100)
    stock_data['MA10'] = stock_data['Close'].rolling(window=10).mean()
    stock_data['MA20'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA100'] = stock_data['Close'].rolling(window=100).mean()

    # Menghitung MACD
    macd = ta.trend.MACD(stock_data['Close'])
    stock_data['MACD'] = macd.macd()
    stock_data['Signal_Line'] = macd.macd_signal()

    # Menghitung RSI
    rsi = ta.momentum.RSIIndicator(stock_data['Close'])
    stock_data['RSI'] = rsi.rsi()

    # Menampilkan grafik harga saham dengan indikator teknikal
    fig, axes = mpf.plot(stock_data, type='candle', title=f'{stock_symbol} Stock Price with Technical Indicators',
                         mav=(10, 20, 50, 100), volume=True, returnfig=True)

    # Menambahkan MACD dan Signal Line
    axes[1].plot(stock_data.index, stock_data['MACD'], color='red', label='MACD')
    axes[1].plot(stock_data.index, stock_data['Signal_Line'], color='blue', label='Signal Line')
    axes[1].legend()

    # Menambahkan RSI
    axes[2].plot(stock_data.index, stock_data['RSI'], color='purple', label='RSI')
    axes[2].axhline(70, color='red', linestyle='--')
    axes[2].axhline(30, color='green', linestyle='--')
    axes[2].legend()

    plt.show()

# Contoh: Analisis teknikal untuk saham Apple (AAPL) pada tahun 2022
stock_symbol = 'TSLA'
start_date = '2022-01-01'
end_date = '2023-07-25'
technical_analysis(stock_symbol, start_date, end_date)
