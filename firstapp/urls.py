from django.urls import path
from .views import *

urlpatterns = [
    path('', homeview, name='homepage'),

    path('cs/', CreateStudentView.as_view(), name='cspage'),
    path('ls/', show_student_view, name='studentpage'),
    path('us/<int:pk>/', UpdateStudentView.as_view(), name='uspage'),
    path('ds/<int:pk>/', DeleteStudentView.as_view(), name='dspage'),

    path('cd/', CreateDepartmentView.as_view(), name='cdpage'),
    path('ld/', show_department_view, name='Departmentpage'),
    path('ud/<int:pk>/', UpdateDepartmentView.as_view(), name='udpage'),
    path('dd/<int:pk>/', DeleteDepartmentView.as_view(), name='ddpage'),

    path('ct/', CreateTeacherView.as_view(), name='ctpage'),
    path('lt/', show_teacher_view, name='Teacherpage'),
    path('ut/<int:pk>/', UpdateTeacherView.as_view(), name='utpage'),
    path('dt/<int:pk>/', DeleteTeacherView.as_view(), name='dtpage'),
]
