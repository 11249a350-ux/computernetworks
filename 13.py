import socket
# Get hostname
hostname = socket.gethostname()
# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
finally:
    s.close()
    print("Host Name :", hostname)
    print("IP Address:", ip_address)

