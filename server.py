import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "0.0.0.0"
PORT = 8820

server_socket.bind((IP, PORT))
server_socket.listen()

print("Server has started running.")

correct_number = random.randint(1, 9)

print("correct number is: " + str(correct_number))

(client_socket, client_IP) = server_socket.accept()

print("A client has connected")


data = ""

while data != "quit":
    client_socket.send("Guess the number  between 0 and 10:".encode())
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    if data == str(correct_number):
        client_socket.send("correct".encode())
        break
    else:
        client_socket.send("incorrect".encode())

client_socket.send("bye".encode())
print("Ending connection with: " + str(client_IP))

client_socket.close()
server_socket.close()