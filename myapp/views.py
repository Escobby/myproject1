from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect


def read_areas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM areas")
        areas = cursor.fetchall()
    return render(request, 'read_areas.html', {'areas': areas})

def create_area(request):
    if request.method == 'POST':
        area_id = request.POST['area_id']
        area_name = request.POST['area_name']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO areas (area_id, area_name) VALUES (%s, %s)", [area_id, area_name])
        return HttpResponseRedirect('/readAreas/')
    return render(request, 'create_area.html')

def update_area(request, area_id):
    if request.method == 'POST':
        new_area_name = request.POST['area_name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE areas SET area_name = %s WHERE area_id = %s", [new_area_name, area_id])
        return HttpResponseRedirect('/readAreas/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT area_name FROM areas WHERE area_id = %s", [area_id])
        area_name = cursor.fetchone()[0]
    return render(request, 'update_area.html', {'area_id': area_id, 'area_name': area_name})

def delete_area(request, area_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM areas WHERE area_id = %s", [area_id])
        return HttpResponseRedirect('/readAreas/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT area_name FROM areas WHERE area_id = %s", [area_id])
        area_name = cursor.fetchone()[0]
    return render(request, 'delete_area.html', {'area_id': area_id, 'area_name': area_name})

######Departments########

def read_departments(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM departments")
        departments = cursor.fetchall()
    return render(request, 'read_departments.html', {'department_list': departments})


def create_department(request):
    if request.method == 'POST':
        department_id = request.POST['department_id']
        department_name = request.POST['department_name']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO departments (department_id, department_name) VALUES (%s, %s)", [department_id, department_name])
        return HttpResponseRedirect('/departments/')
    return render(request, 'create_department.html')


def update_department(request, department_id):
    if request.method == 'POST':
        new_department_name = request.POST['department_name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE departments SET department_name = %s WHERE department_id = %s", [new_department_name, department_id])
        return HttpResponseRedirect('/departments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT department_name FROM departments WHERE department_id = %s", [department_id])
        department_name = cursor.fetchone()[0]
    return render(request, 'update_department.html', {'department_id': department_id, 'department_name': department_name})


def delete_department(request, department_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM departments WHERE department_id = %s", [department_id])
        return HttpResponseRedirect('/departments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT department_name FROM departments WHERE department_id = %s", [department_id])
        department_name = cursor.fetchone()[0]
    return render(request, 'delete_department.html', {'department_id': department_id, 'department_name': department_name})