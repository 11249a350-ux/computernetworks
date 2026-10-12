import socket
import os
def file_transfer_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to server.")
    filename = input("Enter the file name to send: ")
    if not os.path.isfile(filename):
        print("File not found.")
        client_socket.close()
        return
    client_socket.send(filename.encode())
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)
    print(f"File '{filename}' sent successfully.")
    client_socket.close()
if __name__ == '__main__':
    file_transfer_client()