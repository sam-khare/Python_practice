import time
import multiprocessing

def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        ''' since its critical portion as both the function are trying to access shared memory we put lock to avoid
         any inconsistency'''
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    balance = multiprocessing.Value('i',200)
    d = multiprocessing.Process(target=deposit,args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)