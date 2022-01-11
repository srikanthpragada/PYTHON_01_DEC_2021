import threading
from threading import Thread


def print_numbers():
    for i in range(1, 50):
        print(i)


pt = Thread(target=print_numbers)
pt.start()

print(threading.main_thread())
print(threading.active_count())

for i in range(1, 50):
    print(f"Main {i}")
