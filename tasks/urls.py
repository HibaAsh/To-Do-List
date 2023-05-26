from django.urls import path
from . import views 

app_name = "tasks"

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('update/<str:pk>', views.updateTask, name="updateTask"),
    path('delete/<str:pk>', views.deleteTask, name="deleteTask"),
]