# Django-Assignment
About Django Signals.

**Question 1:**
**answer: ** By default, Django signals are executed synchronously. The signal handler blocks execution until it completes.
run then django server. python manage.py runserver. then paste this URL to your browser "http://127.0.0.1:8000/trigger-signal/ . at your terminal, where you will observe that the signal handler runs and introduces a delay of 5 seconds. This confirms that the signal handler executes synchronously, as the view does not finish until the handler completes.
![image](https://github.com/user-attachments/assets/23027db5-9d13-49e8-991c-8797c0906132)

**Question 2:**
**answer: ** Yes, Django signals run in the same thread as the caller by default.
![image](https://github.com/user-attachments/assets/7e4bc79e-77aa-4256-95bb-45a7512f732e)
The output confirms that the signal and the view run in the same thread (MainThread), proving Django signals are not executed in a separate thread by default.

**Question 3:**
**answer: ** Yes, Django signals run in the same database transaction by default. If an error occurs in the signal handler, it will cause the entire transaction to roll back, indicating they are part of the same transaction.
![image](https://github.com/user-attachments/assets/a35fa108-0dbc-415d-bdf7-dc401c5f4468)
![image](https://github.com/user-attachments/assets/276ccc4a-4c99-470f-ae7d-b12468484df5)
![image](https://github.com/user-attachments/assets/5ca9faab-06c3-40e2-b7a1-60fed623837a)


**Topic: Custom Classes in Python**
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)

for dimension in rect:
    print(dimension)


![image](https://github.com/user-attachments/assets/46bdfe0d-3b28-4652-8569-dbe8aa2f835d)

