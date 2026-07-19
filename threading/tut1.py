import threading 
import time 

done = False


def worker():

    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{counter}")


threading.Thread(target=worker).start()

input("press any key to stop>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   ")
done = True  