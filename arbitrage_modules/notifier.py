def alert(profit_info):
    if profit_info is None:
        message = "No profitable trades found."
    else:
        crypto, base_price, lowest_price, exchange_lowest, highest_price, exchange_highest, best_exchange, crypto_direction, difference_percentage = profit_info
        message = f"The lowest price is {lowest_price} at {exchange_lowest} and the highest price is {highest_price} at {exchange_highest}. It is {crypto_direction} by {difference_percentage:.2f}%."

    print(message)
