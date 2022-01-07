from django.shortcuts import render
from .models import Student, Department, Teacher
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy


def homeview(request):
    return render(request, 'firstapp/home.html')


class CreateStudentView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'firstapp/form.html'
    success_url = reverse_lazy('studentpage')


class ListStudentView(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'firstapp/studentlist.html'


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'firstapp/studentdelete.html'
    success_url = reverse_lazy('studentpage')


class UpdateStudentView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('studentpage')
    context_object_name = 'student'
    template_name = 'firstapp/form.html'


class CreateTeacherView(CreateView):
    model = Teacher
    fields = '__all__'
    template_name = 'firstapp/form.html'
    success_url = reverse_lazy('Teacherpage')


class ListTeacherView(ListView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'firstapp/teacherlist.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'firstapp/teacherdelete.html'
    success_url = reverse_lazy('Teacherpage')


class UpdateTeacherView(UpdateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('Teacherpage')
    context_object_name = 'Teacher'
    template_name = 'firstapp/form.html'


class CreateDepartmentView(CreateView):
    model = Department
    fields = '__all__'
    template_name = 'firstapp/form.html'
    success_url = reverse_lazy('Departmentpage')


class ListDepartmentView(ListView):
    model = Department
    context_object_name = 'department'
    template_name = 'firstapp/departmentlist.html'


class DeleteDepartmentView(DeleteView):
    model = Department
    template_name = 'firstapp/departmentdelete.html'
    success_url = reverse_lazy('Departmentpage')


class UpdateDepartmentView(UpdateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('Departmentpage')
    context_object_name = 'Department'
    template_name = 'firstapp/form.html'


def show_student_view(request):
    students = Student.objects.all()
    if request.method == 'POST':
        students = Student.objects.filter(name__icontains=request.POST['data'])
    return render(request, template_name="firstapp/studentlist.html", context={'student': students})


def show_teacher_view(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        teachers = Teacher.objects.filter(name__icontains=request.POST['data'])
    return render(request, template_name="firstapp/teacherlist.html", context={'teacher': teachers})


def show_department_view(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        department = Department.objects.get(name__icontains=request.POST['data'])
        teachers = department.department_teach.all()
        students = department.department_stud.all()
        return render(request, template_name='firstapp/departmentlist.html',
                      context={'department': department, 'teacher': teachers, 'student': students})
    return render(request, template_name="firstapp/departmentlist.html", context={'departments': departments})
