# ch11_01.py
# simple threading

import time
import threading



def perform():
    global prunning

    counter = 0
    prunning = True
    while prunning:
        print('counter:', str(counter))
        time.sleep(2)
        counter += 1

my_thread = threading.Thread(target=perform)
my_thread.setDaemon(True)
my_thread.start()

# python 3
input("按下回车键停止...\n")

# python 2
#raw_input("Press Enter to stop...")

prunning = False
my_thread.join(2)

