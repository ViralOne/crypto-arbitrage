import requests

def get_price(crypto, exchange):
    if exchange == "Binance":
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}USDT"
        response = requests.get(url)
        coin_price = response.json()["price"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Coinbase":
        url = f"https://api.coinbase.com/v2/prices/{crypto}-USD/spot"
        response = requests.get(url)
        coin_price = response.json()["data"]["amount"]
        print(exchange , coin_price + " - " + crypto + "USD")
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

        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bitfinex":
        url = f"https://api.bitfinex.com/v1/ticker/{crypto}usd"
        response = requests.get(url)
        coin_price = response.json()["last_price"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bittrex":
        url = f"https://api.bittrex.com/v3/markets/{crypto}-USD/ticker"
        response = requests.get(url)
        coin_price = response.json()["lastTradeRate"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Huobi":
        crypto = crypto.lower()
        url = f"https://api.huobi.com/market/detail/merged?symbol={crypto}usdt"
        response = requests.get(url)
        coin_price = response.json()["tick"]["close"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Bitstamp":
        crypto = crypto.lower()
        url = f"https://www.bitstamp.net/api/v2/ticker/{crypto}usd/"
        response = requests.get(url)
        coin_price = response.json()["last"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "Cex.io":
        url = f"https://cex.io/api/last_price/{crypto}/USD"
        response = requests.get(url)
        coin_price = response.json()["lprice"]
        print(exchange , coin_price + " - " + crypto + "USD")
        return float(coin_price)
    elif exchange == "TestExchange":
        coin_price = 5
        print(exchange , str(coin_price) + " - " + crypto + "USD")
        return float(coin_price)
    else:
        raise Exception("Exchange not supported")
