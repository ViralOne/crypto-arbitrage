import requests
import time

def get_price(crypto, exchange):
    if exchange == "Binance":
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT"
            response = requests.get(url)
            coin_price = response.json()["price"]
            return float(coin_price)
    elif exchange == "Coinbase":
        url = f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot"
        response = requests.get(url)
        coin_price = response.json()["data"]["amount"]
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
    exchanges = ["Binance", "Coinbase"]
    threshold_percentage = 2 # notify if price has a difference of 2%
    monitor_prices(cryptos, exchanges, threshold_percentage)
