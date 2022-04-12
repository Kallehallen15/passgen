import random
import os
import time
from colorama import Fore, Back, Style
print(Fore.GREEN + 'Welcome to password gen')
time.sleep(3)

os.system("cls")
l = int(input("enter pass lenght: "))
s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = "".join(random.sample(s,l))
os.system("cls")
print ("working online...")
time.sleep(5)
os.system("cls")
print("password :: ",p)