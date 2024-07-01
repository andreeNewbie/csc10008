import socket

HOST = "127.0.0.1"  # localhost
PORT = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("SERVER SIDE: ")
print("Server", HOST, PORT)
print("Waiting for client... \n")

conn, addr = server_socket.accept()

print("client address: ", addr)
print("CONN: ", conn.getsockname())


input()
conn.close()
