import arbitrage_modules.get_price_info as call_exchanges

def check_price(crypto, exchanges, threshold_percentage):
    # Initializing variables
    prices = []
    best_exchange = None
    
    for exchange in exchanges:
        try:
            price = call_exchanges.get_price(crypto, exchange)
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
