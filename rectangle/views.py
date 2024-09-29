from django.shortcuts import render
import time
from django.http import HttpResponse
from .signals import my_signal,my_signal2
from django.db import transaction
import threading
from .models import MyModel

def my_view(request):
    print("View execution started")
    my_signal.send(sender=None)
    print("View execution finished")
    print(f"View thread: {threading.current_thread().name}")
    return HttpResponse("Check your console output")

def my_view2(request):
    try:
        with transaction.atomic():
            MyModel.objects.create(name="Test")
            my_signal2.send(sender=None)
    except Exception as e:
        return HttpResponse(f"Error: {e}")
    return HttpResponse("Signal sent")