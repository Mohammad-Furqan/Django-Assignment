import time
from django.dispatch import Signal, receiver
import threading

my_signal = Signal()
my_signal2 = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started")
    time.sleep(5) 
    print(f"Signal handler thread: {threading.current_thread().name}")
    print("Signal handler finished")
    raise Exception("Force rollback in signal handler")


@receiver(my_signal2)
def my_signal_handler(sender, **kwargs):
    print("Signal handler started")
    raise Exception("Force rollback in signal handler")

