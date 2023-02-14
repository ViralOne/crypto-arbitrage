import time
import arbitrage_modules.notifier as notifications
import arbitrage_modules.checker as check

def monitor_prices(cryptos, exchanges, threshold_percentage):
    while True:
        for crypto in cryptos:
            profit_info = check.check_price(crypto, exchanges, threshold_percentage)
            if profit_info:
                notifications.alert(profit_info)
        time.sleep(60) # check prices every 60 seconds
