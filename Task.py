import threading
import time

start=time.perf_counter()

def func():
    i=0
    while True:
        print(i)
        i=i+1
        global stop_threads
        if stop_threads:
            global last
            last=i
            break
 
stop_threads = False
t1 = threading.Thread(target = func)
t1.start()

# Stop main thread for 1 second
time.sleep(1)

# Stop thread after returning to main thread
stop_threads = True
t1.join()
finish=time.perf_counter()

print('Thread killed')
print('Last number printed = %d' %(last-1))
print(f'Finished in {round(finish-start, 2)} second(s)')