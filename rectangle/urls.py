from django.urls import path
from . import views

urlpatterns = [
    path('trigger-signal/', views.my_view, name='trigger_signal'),
    path('transaction-signal/', views.my_view2, name='transaction_signal'), 
]
