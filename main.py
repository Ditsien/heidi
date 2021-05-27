# https://blog.ipswitch.com/how-to-create-a-computer-inventory-script-in-python-for-linux-macos

# importerede moduler
import os
import platform
import socket
import shutil
import psutil
from contextlib import redirect_stdout
from datetime import datetime

# Systemnavn og release
platform.system()
platform.release()

# Først hostnavn, og så lav hostnavn om til IP
socket.gethostname()
socket.gethostbyname(socket.gethostname())

svmem = psutil.virtual_memory()
disk = shutil.disk_usage('/')

# Funktion til at konvertere bytes
# https://www.thepythoncode.com/article/get-hardware-system-information-python
def get_size(bytes, suffix="B"):
    
        #1253656 ==> '1.20MB'
        #1253656678 ==> '1.17GB'
   
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#Gemmer i en fil
# Log sti
log_sti = '/Users/hsc/Documents/H5_skole/'

with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print('Local IP address: {0}'.format(socket.gethostbyname(socket.gethostname())))
        print('OS: {0} {1}'.format(platform.system(), platform.release()))

# Diskplads:
        print(f"Used disk space: {get_size(disk.used)}")
        print(f"Available disk space: {get_size(disk.free)}")
        print(f"Total disk space: {get_size(disk.total)}")

    # Memory Information

        print(f"Total Memory: {get_size(svmem.total)}")
        print(f"Available memory: {get_size(svmem.available)}")
        print(f"Used memory: {get_size(svmem.used)}")
        print(f"Percentage memory used: {svmem.percent}%")
f.close()

datefmt='%d-%m-%Y %H.%M.%S'
shutil.copy('/Users/hsc/PycharmProjects/Project_H5/output.txt', log_sti)
os.rename(r'' + log_sti + 'output.txt', r'' + log_sti + datetime.now().strftime(datefmt) + '.txt')
format='%(asctime)s %(message)s'
