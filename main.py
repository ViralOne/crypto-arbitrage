import requests
import time

def get_price(crypto, exchange):
    if exchange == "Binance":
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT"
            response = requests.get(url)
            coin_price = response.json()["price"]
            print("Binance: " + coin_price + " - " + crypto + "USD")
            return float(coin_price)
    elif exchange == "Coinbase":
        url = f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot"
        response = requests.get(url)
        coin_price = response.json()["data"]["amount"]
        print("Coinbase: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Kraken":
        pair_code = None
        if crypto == "BTC":
            pair_code = "XXBTZ"
        elif crypto == "ETH":
            pair_code = "XETHZ"
        
        url = f"https://api.kraken.com/0/public/Ticker?pair={crypto}USD"
        response = requests.get(url)    
        
        if pair_code is None:
            coin_price = response.json()["result"][f"{crypto}USD"]["c"][0]
        else:
            coin_price = response.json()["result"][f"{pair_code}USD"]["c"][0]

        print("Kraken: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bitfinex":
        url = f"https://api.bitfinex.com/v1/ticker/{crypto}usd"
        response = requests.get(url)
        coin_price = response.json()["last_price"]
        print("Bitfinex: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bittrex":
        url = f"https://api.bittrex.com/v3/markets/{crypto}-USD/ticker"
        response = requests.get(url)
        coin_price = response.json()["lastTradeRate"]
        print("Bittrex: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Huobi":
        crypto = crypto.lower()
        url = f"https://api.huobi.com/market/detail/merged?symbol={crypto}usdt"
        response = requests.get(url)
        coin_price = response.json()["tick"]["close"]
        print("Huobi: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bitstamp":
        crypto = crypto.lower()
        url = f"https://www.bitstamp.net/api/v2/ticker/{crypto}usd/"
        response = requests.get(url)
        coin_price = response.json()["last"]
        print("Bitstamp: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Cex.io":
        url = f"https://cex.io/api/last_price/{crypto}/USD"
        response = requests.get(url)
        coin_price = response.json()["lprice"]
        print("Cex.io: " + coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "test":
        coin_price = 5
        print(coin_price)
        return float(coin_price)
    else:
        raise Exception("Exchange not supported")

def check_price(crypto, exchanges, threshold_percentage):
    # Initializing variables
    prices = []
    best_exchange = None
    
    for exchange in exchanges:
        try:
            price = get_price(crypto, exchange)
            if price is not None:
                prices.append((price, exchange))
        except:
            continue
    
    if len(prices) == 0:
        return None
    
    base_price, _ = min(prices)
    highest_price, exchange_highest = max(prices)
    lowest_price, exchange_lowest = min(prices)
    
    difference_percentage = (highest_price / base_price - 1) * 100
    
    if difference_percentage > threshold_percentage:
        if highest_price == prices[-1][0]:
            crypto_direction = "higher"
            best_exchange = exchange_highest
        else:
            crypto_direction = "lower"
            best_exchange = exchange_lowest
    else:
        return None
    
    return crypto, base_price, lowest_price, exchange_lowest, highest_price, exchange_highest, best_exchange, crypto_direction, difference_percentage

def notify(profit_info):
    if profit_info is None:
        message = "No profitable trades found."
    else:
        crypto, base_price, lowest_price, exchange_lowest, highest_price, exchange_highest, best_exchange, crypto_direction, difference_percentage = profit_info
        message = f"The lowest price is {lowest_price} at {exchange_lowest} and the highest price is {highest_price} at {exchange_highest}. It is {crypto_direction} by {difference_percentage:.2f}%."

    print(message)


def monitor_prices(cryptos, exchanges, threshold_percentage):
    while True:
        for crypto in cryptos:
            profit_info = check_price(crypto, exchanges, threshold_percentage)
            if profit_info:
                notify(profit_info)
        time.sleep(60) # check prices every 60 seconds

if __name__ == "__main__":
    cryptos = ["SOL", "ADA"]
    exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex", "Bittrex", "Bitstamp", "Cex.io", "test"]
    threshold_percentage = 1 # notify if price has a difference of 5%
    monitor_prices(cryptos, exchanges, threshold_percentage)
