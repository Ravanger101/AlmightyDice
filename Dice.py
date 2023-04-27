import random
import sys
from time import sleep

x = "y"

while x == "y":
    no = random.randint(1,6)
    if no == 1:
        print(end='You rolled 1!\n')
        sys.stdout.flush()
        sleep(1)
    if no == 2:
        print(end='You rolled 2!\n')
        sys.stdout.flush()
        sleep(1)
    if no == 3:
        print(end='You rolled 3!\n')
        sys.stdout.flush()
        sleep(1)
    if no == 4:
        print(end='You rolled 4!\n')
        sys.stdout.flush()
        sleep(1)
    if no == 5:
        print(end='You rolled 5!\n')
        sys.stdout.flush()
        sleep(1)
    if no == 6:
        print(end='You rolled 6!\n')
        sys.stdout.flush()
        sleep(1)
        
    x=input("Type y to roll dice.\n")