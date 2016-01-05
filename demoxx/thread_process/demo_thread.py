import threading
import time
def print_time():
    while 1:
      time.sleep(2)
      print ("%s: %s" % (t1, time.ctime(time.time())))
      print ("%s: %s" % (t2, time.ctime(time.time())))
#Start threads to print time at different intervals
t1 = threading.Thread(target=print_time, name='Thread01')
t2 = threading.Thread(target=print_time, name='Thread02')
t1.start()
t2.start()
t1.join()
t2.join()

