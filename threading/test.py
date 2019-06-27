import time
import threading


start = time.time()


def dummy_task(period):
    print(f"dummy task started, with period {period}")
    time.sleep(period)
    print(f"dummy task wokeup, period {period}")


t = threading.Thread(target=dummy_task,name="first thread", args=(5,))
t.start()

t = threading.Thread(target=dummy_task,name="first thread", args=(2,))
t.start()

t = threading.Thread(target=dummy_task,name="first thread", args=(9,))
t.start()