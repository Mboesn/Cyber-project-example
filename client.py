import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "127.0.0.1"
PORT = 8820

sock.connect((IP, PORT))

data = ""

while data != "bye":
    data = sock.recv(1024).decode()
    print("The server sent: " + data)

    if data == "bye":
        break

    output = input()
    sock.send(output.encode())
    data = sock.recv(1024).decode()
    print("The server sent: " + data)

sock.close()