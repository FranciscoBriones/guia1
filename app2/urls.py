from django.urls import path
from . import views

urlpatterns = [
    path('testeo/', views.testeo),
    path('belsema/', views.belsemaa)
]