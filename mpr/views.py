from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Import the Registration model
from django.db.models import Max,Min
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from datetime import date as d, datetime as dt
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib import messages



def index(request):
    return render(request, "index.html")
def register(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phoneno']
        password1=request.POST['password']
        image1=request.FILES['image']
        address1=request.POST['address']
        if User.objects.filter(Q(Email=email1) | Q(Phonenumber=phonenumber1)).exists():
            messages.info(request,"Already Have Registered")
        else:
            user=Login.objects.create(
            view_email=email1,view_password=password1,user_type='user',is_active="0")
            user.save()
            register=User.objects.create(
            Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,Image=image1,Address=address1,user=user)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login_1")
    return render(request, "register.html")
def Employee_register(request):
    if request.POST:
        username2=request.POST['username1']
        email2=request.POST['email1']
        phonenumber2=request.POST['phoneno1']
        password2=request.POST['password1']
        image2=request.FILES['image1']
        address2=request.POST['address1']
        if Employee.objects.filter(Email1=email2).exists():
            messages.info(request,"Already Have Registered")
        else:
            employee=Login.objects.create(
            view_email=email2,view_password=password2,user_type='employee',is_active="0")
            employee.save()
            register1=Employee.objects.create(
            Username1=username2,Email1=email2,Phonenumber1=phonenumber2,Password1=password2,Image1=image2,Address1=address2,employee=employee)
            register1.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login_1")
    return render(request, "Employee_register.html")
from django.core.exceptions import ObjectDoesNotExist

def login_1(request):
    if request.POST:
        Email3 = request.POST['email3']
        Password3 = request.POST['password3']
        try:
            user = Login.objects.get(view_email=Email3)
            if user.view_password == Password3:
                if user.user_type == "admin":
                    messages.info(request, "Welcome To the Admin Page")
                    return redirect("/adminhome")
                elif user.user_type == "user":
                    request.session['uid'] = user.id
                    messages.info(request, "Welcome To the User Page")
                    return redirect("/userhome")
                elif user.user_type == "employee":
                    request.session['uid'] = user.id
                    messages.info(request, "Welcome To the Employee Page")
                    return redirect("/employeehome")
                else:
                    messages.info(request, "Invalid Username Or Password")
                    return redirect("/login_1")
            else:
                messages.info(request, "Invalid Password")
                return redirect("/login_1")
        except ObjectDoesNotExist:
            messages.info(request, "Invalid Username Or Password")
            return redirect('/login_1')
    return render(request, "login_1.html")

#admin

def adminhome(request):
    return render(request,"Admin/adminhome.html")

def admin_view_employee(request):
    data=Employee.objects.all()
    return render(request,"Admin/admin_view_employee.html",{"data":data})
def admin_view_users(request):
    data=User.objects.all()
    return render(request,"Admin/admin_view_users.html",{"data":data})

from django.contrib import messages
from django.shortcuts import redirect
from .models import User

def actionusers(request):
    id = request.GET.get('id')  # Use get() method to avoid KeyError if 'id' is not in the request
    user = User.objects.get(id=id)
    user.status = 'Approved'  # Update the status attribute directly
    user.save()  # Save the changes to the database
    messages.info(request, "Approved Successfully")
    return redirect("/admin_view_users")
def rejectusers(request):
    id=request.GET.get('id')
    s=User.objects.get(id=id)
    login_id = s.user_id
    
    e=Login.objects.get(id=login_id).delete()
    s.delete()
    messages.info(request,"Rejected successfully")
    return redirect("/admin_view_users")
def deleteusers(request):
    id=request.GET['id']
    r=User.objects.get(id=id)
    login_id =r.user_id
    q=Login.objects.get(id=login_id)
    q.delete()
    r.delete()
    messages.info(request,"User Deleted Successfully")
    return redirect("/admin_view_users")

from django.contrib import messages
from django.shortcuts import redirect
from .models import Employee

def actionemployee(request):
    id = request.GET.get('id')  # Use get() method to avoid KeyError if 'id' is not in the request
    employee = Employee.objects.get(id=id)
    employee.status = 'Approved'  # Update the status attribute directly
    employee.save()  # Save the changes to the database
    messages.info(request, "Approved Successfully")
    return redirect("/admin_view_employee")

def rejectemployee(request):
    id=request.GET.get('id')
    g=Employee.objects.get(id=id)
    login_id = g.employee_id
    
    e=Login.objects.get(id=login_id).delete()
    g.delete()
    messages.info(request,"Rejected successfully")
    return redirect("/admin_view_employee")
def deleteemployee(request):
    id=request.GET['id']
    n=Employee.objects.get(id=id)
    login_id =n.employee_id
    r=Login.objects.get(id=login_id)
    r.delete()
    n.delete()
    messages.info(request,"Employee Deleted Successfully")
    return redirect("/admin_view_employee")


def admin_vieworders(request):
    data=Request.objects.all()
    return render(request,"Admin/admin_vieworders.html",{"data":data})

def admin_add_employee(request):
    order_id =request.GET['order_id']
    data=Employee.objects.all()
    return render(request,"Admin/admin_add_employee.html",{"data":data,'order_id':order_id})
def add_emp(request):
    try:
        employee_id = request.GET['id']
        order_id = request.GET['order_id']

        # Fetch the employee and the request
        employee = Employee.objects.get(id=employee_id)
        request_obj = Request.objects.get(id=order_id)

        # Assign the employee to the request and save
        request_obj.employee = employee
        request_obj.save()

        # Inform the user of success and redirect
        messages.info(request, "Employee added successfully")
        return redirect('/admin_vieworders')
    
    except (Employee.DoesNotExist, Request.DoesNotExist, KeyError) as e:
        messages.error(request, "An error occurred while adding employee: {}".format(str(e)))
        return redirect('/admin_vieworders')



    except (ObjectDoesNotExist, KeyError) as e:
        # Handle any errors (e.g., missing employee or request, missing parameters)
        messages.error(request, "Failed to add employee. Please try again.")
        return redirect('Admin/vieworders')  # Redirect to appropriate page


#user
def userhome(request):
    return render(request,"User/userhome.html")
def addrequest(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    #id = request.GET.get("id")
    #employee = Employee.objects.get(id=id)
    if request.POST:
        servise=request.POST['servise']
        date=request.POST['date']
        phone=request.POST['phone']
        time=request.POST['time']
        am_pm=request.POST['am_pm']

        data=Request.objects.create(Datetime=date,user=user,Time =time,Phone = phone,am_pm = am_pm,Service=servise)
        data.save()
        messages.info(request,"Send Request successfully")
        return redirect('/userhome')
    return render(request,"User/addrequest.html")

def viewrequest_user(request):
    uid=request.session['uid']
    print(uid)
    user=User.objects.get(user=uid)
    data=Request.objects.filter(user=user)
    return render(request,"User/viewrequest_user.html",{"data":data})
def cancel(request):
    id=request.GET['id']
    a=Request.objects.get(id=id)
    a.status = 'canceled'
    a.save()
    messages.info(request,"Canceled Successfully")
    return redirect("/viewrequest_user")

def addpayment(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    id = request.GET.get('id')
    employee = Employee.objects.get(request__id=id)
    if request.method == 'POST':
        payment = Payment(user=user,employee=employee,status="paid")
        payment.save()
        r =Request.objects.get(id=id)
        r.status='paid'
        r.save()
        messages.info(request,"Paid successfully")
        return redirect('/viewrequest_user')
    return render(request, "User/addpayment.html")
def view_services(request):
    return render(request,"User/view_services.html")

#employee
def employeehome(request):
    return render(request,"Employee/employeehome.html")

def employee_viewrequest(request):
    uid=request.session['uid']
    employee=Employee.objects.get(employee=uid)
    employee_id=employee.id
    data=Request.objects.filter(employee=employee_id)
    return render(request,"Employee/employee_viewrequest.html",{"data":data})

def actionrequest(request):
    id=request.GET['id']
    if request.POST:
        price1=request.POST['price']
        y=Request.objects.filter(id=id).update(Price=price1,status='Approved')
        messages.info(request,"Price Add And Approved Successfully")
        return redirect("/employee_viewrequest")
    return render(request,"Employee/addprice.html")

def viewpayment(request):
    uid=request.session['uid']
    employee=Employee.objects.get(employee_id=uid)
    employee_id =employee.id
    print(employee_id)
    data=Payment.objects.filter(employee_id =employee_id)
    return render(request,"Employee/viewpayment.html",{"data":data})