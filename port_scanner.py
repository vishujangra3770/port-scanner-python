import socket
import threading

target = input("Enter target: ")

def scan(port):
    sock = socket.socket()
    socket.setdefaulttimeout(1)
    
    if sock.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} open")
    
    sock.close()

print(f"Scanning {target}...\n")

for port in range(1, 1025):
    thread = threading.Thread(target=scan, args=(port,))
    thread.start()
