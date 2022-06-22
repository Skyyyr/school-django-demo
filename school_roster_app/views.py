from django.shortcuts import render

# Create your views here.

from school_roster_app.models import School

my_school = School("Django School")


def index(request):
    my_data = {
        "school_name": my_school.name
    }
    return render(request, 'pages/index.html', my_data)


def list_staff(request):
    my_data = {
        'staff': my_school.staff
    }
    return render(request, 'pages/list_staff.html', my_data)


def staff_detail(request, employee_id):
    my_data = {
        'staff': School.find_staff_by_id(my_school, employee_id)
    }
    return render(request, 'pages/find_staff.html', my_data)


def list_students(request):
    my_data = {
        'student': my_school.students
    }
    return render(request, 'pages/list_students.html', my_data)


def student_detail(request, student_id):
    my_data = {
        'student': School.find_student_by_id(my_school, student_id)
    }
    return render(request, 'pages/find_student.html', my_data)
