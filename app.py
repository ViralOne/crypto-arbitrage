import arbitrage_modules.monitor as monitor

exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex", "Bittrex", "Bitstamp", "Cex.io", "TestExchange"]
cryptos = ["SOL"]
threshold_percentage = 2 # notify if price has a difference of 2%

if __name__ == "__main__":
    monitor.monitor_prices(cryptos, exchanges, threshold_percentage)
