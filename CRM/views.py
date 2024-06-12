from django.shortcuts import render, redirect
from .forms import CreateUserForm, loginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record

from django.contrib import messages

from django.http.response import JsonResponse

# - Homepage

def home(request):

    return render(request, 'CRM/index.html')

# - Register a user

def Register(request):

    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()

            messages.success(request, "Account created successfully")

            return redirect('')
    
    context = {'form':form}

    return render(request, 'CRM/register.html', context=context)


# - Login a user

def my_login(request):

    form = loginForm()

    if request.method =="POST":

        form = loginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')
    
    context = {'form':form}

    return render(request, 'CRM/my-login.html', context=context)

# - User logout

@login_required(login_url='my-login')
def user_logout(request):

    auth.logout(request)

    messages.success(request, "logout success")

    return redirect('my-login')

# - Dashboard

def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'CRM/dashboard.html', context=context)


# - For Data Table

def dashboardJSON(request):

    my_records = list(Record.objects.values())

    data={'records': my_records} 

    return JsonResponse(data)

# - Create a record

@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'CRM/create-record.html', context=context)
    
# - Update a record

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            
            form.save()

            messages.success(request, "Your record was updated")

            return redirect('dashboard')
    
    context = {'form':form}

    return render(request, 'CRM/update-record.html', context=context)
        
# - Read / View a singular record
@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'CRM/view-record.html', context=context)

# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted")

    return redirect('dashboard')




