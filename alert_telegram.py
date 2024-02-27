import requests
from dataclasses import dataclass
#This code can be used alongside the IB API to send the order & stop order values as an alert to Telegram

TOKEN = "6715483549:AAG2DvHuNsPwxozslwmGm7fPevNqB_m-nS0"
#url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#print(requests.get(url).json()) #get chat_id
chat_id = 533402305
#message = "hello from your telegram bot"

def send(pair, order, stop_order):
    #Replace token, chat_id & text variables
    text = f'A new trade has been placed in {pair} at {order.limitPrice} with a stop at {stop_order.auxPrice}'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    print(requests.get(url).json()) # this sends the message
    #token = '6715483549:AAG2DvHuNsPwxozslwmGm7fPevNqB_m-nS0'
    #params = {'chat_id': '@AndyGrigo', 'text': text, 'parse_mode': 'HTML'}
    #resp = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(token), params)
    #resp.raise_for_status()
@dataclass
class order:
    name: str='BUY'
    limitPrice = 99
@dataclass
class stop_order:
    name: str='stoporder'
    auxPrice = 97

send('EURUSD', order, stop_order)