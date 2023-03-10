from django.shortcuts import render
from .models import School

my_school = School("Django School")


def index(request):
    my_data = {
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {
        "staff": my_school.staff
    }
    return render(request, "pages/index.html", my_data)


def all_staff(request):
    my_data = {
        "staff": my_school.staff
    }
    return render(request, "pages/all_staff.html", my_data)


def staff_detail(request, employee_id):
    my_data = {
        "staff_member": School.find_staff_by_id(my_school, employee_id)
    }

    return render(request, "pages/staff_detail.html", my_data)


def list_students(request):
    my_data = {
        "school_students": my_school.students
    }
    return render(request, "pages/index.html", my_data)


def student_detail(request, student_id):
    my_data = {
        "student": School.find_student_by_id(my_school, student_id)
    }

    return render(request, "pages/student_detail.html", my_data)
