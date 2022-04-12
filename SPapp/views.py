from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib import messages
from SPapp.forms import login_register, studentregisterform
from SPapp.models import Register_details

def home(request):
    data = Register_details.objects.all()
    return render(request,'home.html',{ 'data':data })

def studentregform(request):
    form =studentregisterform()
    form2 =login_register()
    if request.method == 'POST':
        form =studentregisterform(request.POST) 
        form2 =login_register(request.POST) 
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            a = form2.save(commit=False)
            a.user = user
            a.save()
            messages.info(request,"added")
    return render(request,'Student_reg_form.html',{'form':form,'form2':form2})

def loginpage(request):
    return render(request,'loginpage.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_student:
                
                return redirect('studentdetails')
    else:
         messages.info(request,"invalid credentials")
    return render(request,'loginpage.html')  

 
def studentdetails(request):
    data = Register_details.objects.all()
    return render(request,'studentdetails.html',{'data':data})


# Create your views here.
# Superuser= amal : amal@123

