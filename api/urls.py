from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListCreate.as_view(), name='student-list'),
    path('student/<int:pk>', views.StudentDelete.as_view(), name='student-delete'),
]
