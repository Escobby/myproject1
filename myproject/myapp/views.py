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
        return HttpResponseRedirect('/readDepartments/')
    return render(request, 'create_department.html')


def update_department(request, department_id):
    if request.method == 'POST':
        new_department_name = request.POST['department_name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE departments SET department_name = %s WHERE department_id = %s", [new_department_name, department_id])
        return HttpResponseRedirect('/readDepartments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT department_name FROM departments WHERE department_id = %s", [department_id])
        department_name = cursor.fetchone()[0]
    return render(request, 'update_department.html', {'department_id': department_id, 'department_name': department_name})


def delete_department(request, department_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM departments WHERE department_id = %s", [department_id])
        return HttpResponseRedirect('/readDepartments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT department_name FROM departments WHERE department_id = %s", [department_id])
        department_name = cursor.fetchone()[0]
    return render(request, 'delete_department.html', {'department_id': department_id, 'department_name': department_name})

######SubDepartments########
def read_subdepartments(request):
    search_query_id = request.GET.get('search_id', '')
    search_query_name = request.GET.get('search_name', '')

    query = "SELECT * FROM subdepartments"
    params = []

    if search_query_id or search_query_name:
        filters = []
        if search_query_id:
            filters.append("subdepartment_id LIKE %s")
            params.append(f'%{search_query_id}%')
        if search_query_name:
            filters.append("subdepartment_name LIKE %s")
            params.append(f'%{search_query_name}%')
        
        query += " WHERE " + " AND ".join(filters)

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        subdepartments = cursor.fetchall()

    return render(request, 'read_subdepartments.html', {
        'subdepartment_list': subdepartments,
        'search_query_id': search_query_id,
        'search_query_name': search_query_name
    })

def create_subdepartment(request):
    if request.method == 'POST':
        subdepartment_id = request.POST['subdepartment_id']
        subdepartment_name = request.POST['subdepartment_name']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO subdepartments (subdepartment_id, subdepartment_name) VALUES (%s, %s)", [subdepartment_id, subdepartment_name])
        return HttpResponseRedirect('/readSubdepartments/')
    return render(request, 'create_subdepartment.html')

def update_subdepartment(request, subdepartment_id):
    if request.method == 'POST':
        new_subdepartment_name = request.POST['subdepartment_name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE subdepartments SET subdepartment_name = %s WHERE subdepartment_id = %s", [new_subdepartment_name, subdepartment_id])
        return HttpResponseRedirect('/readSubdepartments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT subdepartment_name FROM subdepartments WHERE subdepartment_id = %s", [subdepartment_id])
        subdepartment_name = cursor.fetchone()[0]
    return render(request, 'update_subdepartment.html', {'subdepartment_id': subdepartment_id, 'subdepartment_name': subdepartment_name})

def delete_subdepartment(request, subdepartment_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM subdepartments WHERE subdepartment_id = %s", [subdepartment_id])
        return HttpResponseRedirect('/readSubdepartments/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT subdepartment_name FROM subdepartments WHERE subdepartment_id = %s", [subdepartment_id])
        subdepartment_name = cursor.fetchone()[0]
    return render(request, 'delete_subdepartment.html', {'subdepartment_id': subdepartment_id, 'subdepartment_name': subdepartment_name})

######Machines#######

def read_machines(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM machines")
        machines = cursor.fetchall()
    return render(request, 'read_machines.html', {'machine_list': machines})

def create_machine(request):
    if request.method == 'POST':
        machine_id = request.POST['machine_id']
        machine_name = request.POST['machine_name']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO machines (machine_id, machine_name) VALUES (%s, %s)", [machine_id, machine_name])
        return HttpResponseRedirect('/readMachines/')
    return render(request, 'create_machine.html')

def update_machine(request, machine_id):
    if request.method == 'POST':
        new_machine_name = request.POST['machine_name']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE machines SET machine_name = %s WHERE machine_id = %s", [new_machine_name, machine_id])
        return HttpResponseRedirect('/readMachines/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT machine_name FROM machines WHERE machine_id = %s", [machine_id])
        machine_name = cursor.fetchone()[0]
    return render(request, 'update_machine.html', {'machine_id': machine_id, 'machine_name': machine_name})

def delete_machine(request, machine_id):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM machines WHERE machine_id = %s", [machine_id])
        return HttpResponseRedirect('/readMachines/')
    with connection.cursor() as cursor:
        cursor.execute("SELECT machine_name FROM machines WHERE machine_id = %s", [machine_id])
        machine_name = cursor.fetchone()[0]
    return render(request, 'delete_machine.html', {'machine_id': machine_id, 'machine_name': machine_name})