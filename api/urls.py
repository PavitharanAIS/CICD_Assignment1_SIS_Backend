from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListCreate.as_view(), name='student-list'),
    path('student/<int:pk>', views.StudentDelete.as_view(), name='student-delete'),
    path('lecturer/', views.LecturerListCreate.as_view(), name='lecturer-list'),
    path('lecturer/<int:pk>', views.LecturerDelete.as_view(), name='lecturer-delete'),
    path('programme/', views.ProgrammeListCreate.as_view(), name='programme-list'),
    path('programme/<int:pk>', views.ProgrammeDelete.as_view(), name='programme-delete'),
    path('marks/', views.MarksListCreate.as_view(), name='marks-list'),
    path('marks/<int:pk>', views.MarksDelete.as_view(), name='marks-delete'),
    path('tuitionfee/', views.TuitionFeeListCreate.as_view(), name='tuitionfee-list'),
    path('tuitionfee/<int:pk>', views.TuitionFeeDelete.as_view(), name='tuitionfee-delete'),
]
