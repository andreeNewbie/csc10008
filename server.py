from dotenv import load_dotenv

load_dotenv()

import socket
import threading
import time
from db import connect_database

HOST = "127.0.0.1"  # localhost
PORT = 3000
clients_list = []
limit = 3


class Server:
    db_message, user_col = connect_database()
    print(db_message)

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen()
        print("SERVER SIDE: ")
        print("Server", HOST, PORT)
        print("Waiting for client... \n")

    def connect(self, conn, addr):
        print("client address: ", addr)
        print("CONN: ", conn.getsockname())
        input()
        print("Disconnect client", len(clients_list))
        conn.close()
        clients_list.remove(threading.current_thread())

    def handle_clients(self):
        while len(clients_list) < limit:
            conn, addr = self.server_socket.accept()
            thr = threading.Thread(target=self.connect, args=(conn, addr))
            thr.start()
            clients_list.append(thr)
            print(f"Connected clients: {len(clients_list)}")
            time.sleep(0.1)

        print("Maximum clients reached. Cannot accept more connections.")
        self.server_socket.close()


if __name__ == "__main__":
    server = Server()
    server.handle_clients()
