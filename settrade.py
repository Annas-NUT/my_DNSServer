import time
import requests
import yfinance as yf
#stock_data = yf.history(ticker="GOOGL")

def send_line_notify(message, token):
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message': message
    }
    response = requests.post(line_notify_api, headers=headers, data=data)
    return response.status_code

token = 't1C76kuW1qnUFpghQMQndumbfhmrQhrWtSW1gWbuvp6'
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {token}",
}

want=10
STOCK_1 = "GOOGL"
old_price = 0
first_stock_data = yf.download(tickers=STOCK_1, period="1d", interval="1m")
first_current_price = first_stock_data["Close"].iloc[-1]
while True:
    real_stock_data = yf.download(tickers=STOCK_1, period="1d", interval="1m")
    print(real_stock_data)
    current_price = real_stock_data["Close"].iloc[-1]
    if old_price !=0:
        diff_price = current_price - first_current_price
        if diff_price>=want:
            message = (
                f"Old price: ${old_price:.3f}\n"
                + f"First current price: ${current_price:.3f}\n"
                + f"Difference: ${diff_price:.3f}"
                + f"The price of google has increased to over {want}\n"
            )
        else:
            message = (
                f"Old price: ${old_price:.3f}\n"
                +f"First current price: ${current_price:.3f}\n"
                +f"Difference: ${diff_price:.3f}")
            pass
    else:
        message = f"The price of google is ${current_price:.3f}"
    line_notify_api="https://notify-api.line.me/api/notify"
    data={"message": message}
    response = requests.post(line_notify_api, headers=headers, data=data)
    old_price = current_price

    time.sleep(60)