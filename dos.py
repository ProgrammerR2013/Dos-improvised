# import the packages
from platform import system
import os
import time
import random
import socket
from urllib import request
import sys

path = os.getcwd()
path = os.path.join(path, "lib")
sys.path.append(path)
import coloroma
from coloroma import Fore, Back
from tqdm.auto import tqdm

de_version = "1.1"
coloroma.init()
# platform info
uname = system()
if uname== "Windows":
  cmd ="cls"
else:
  cmd = "clear"
os.system(cmd)
##############
sock = socket.socket(socket.AF_INET, socket.SOC_DGRAM)
bytes = random._urandom(1490)


#############
