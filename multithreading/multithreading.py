## Multithreading 
## I/O bound tasks: Tasks that spend more time waiting for I/O operations(ef file operation , network requests)
## concurent operations and improve throughput of your application by multiple operation concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number :{i}")
        
        
def print_letter():
    for letter in "abcde":
        time.sleep(1)
        print(f"letter : {letter}")
        
        
        
## create 2 threads
t1= threading.Thread(target = print_numbers)## to run them  concurrently 
t2= threading.Thread(target= print_letter)


t=time.time()
## start the thread
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

### wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time()- t
print(finished_time)

