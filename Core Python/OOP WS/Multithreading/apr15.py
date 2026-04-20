'''
Multithreading ----> Multithreading in Python means running multiple threads (small units of a 
                     program) at the same time within a single process to perform tasks concurrently.

Think of it like this:
Instead of doing one task after another, your program can do multiple tasks “simultaneously” 
(or appear to do so), which improves performance—especially for tasks like waiting (I/O operations).

        3 Ghz = 3 * 10^9 Hz
        1 sec = 1000 milisecond

        multitasking --> ruuning many application at a time
        multithreading --> ruuning many task on same application

import threading, time

Thread class
run method  -> override
start method -> strat one thread
                internally invoke run mehtod

join method --> main thread wait until the thread which called is completed

'''
import threading
import time

class MyThread(threading.Thread):
    balance = 1000
    lock = threading.Lock()

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):

        for i in range(5):
            print(threading.current_thread().name)
            time.sleep(3)
            print("sakshi")

    def withdraw(self,amount):
          with MyThread.lock:
                MyThread.balance = MyThread.balance- amount

t1 = MyThread("Thread-1")
t1.start()

t1.join()

for i in range(5):
            print(threading.current_thread().name)
            print("sojar")