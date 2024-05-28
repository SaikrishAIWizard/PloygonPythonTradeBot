# API key
polygonAPIkey = "8ZFPI0zT3iXNMmm4cg8KOmweeRsuEMo9"  # Replace 'your_api_key_here' with your actual API key

from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

# subscribes to all trades
c = WebSocketClient(api_key = polygonAPIkey,subscriptions=["T.*"])

def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)

c.run(handle_msg)