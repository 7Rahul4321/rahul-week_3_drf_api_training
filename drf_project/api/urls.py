from django.urls import path
from .views import home, update_student, delete_student

urlpatterns = [
    path('', home),
    path('update/<int:pk>/', update_student),
    path('delete/<int:pk>/', delete_student),
]