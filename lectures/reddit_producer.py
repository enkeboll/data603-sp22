import time
import socket
import json

import requests

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 22223        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
        while True:
            resp_dict = requests.get('https://www.reddit.com/r/AskReddit.json', headers=header).json()
            
            for topic in resp_dict.get('data', {}).get('children', []):
                payload = {'id': topic.get('data').get('id'),
                           'score': topic.get('data').get('score')}
                conn.sendall(str.encode(json.dumps(payload)+'\n'))
            time.sleep(3)
