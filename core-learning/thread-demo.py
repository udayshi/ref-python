import threading
import time
shared_variable = 0
lock = threading.Lock()

def worker():
    global shared_variable
    time.sleep(3)
    
    with lock:
        shared_variable += 1
    print(f"v: {shared_variable}")
    

threads = []
for _ in range(20):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(shared_variable)