from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import signupForm,HabitForm
from .models import HabitModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

#This function is for signup_form
def sign_up(request):
    if request.method == "POST":
        fm = signupForm(request.POST)
        # phn = UserPhoneForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Register Successfully !")
            fm.save()
            return HttpResponseRedirect('/signup/')
        # if phn.is_valid():
        #     phn.save()
    else:
        fm = signupForm()
        # phn = UserPhoneForm()
    return render(request, 'signup.html', {'form': fm})


#This function is for login_form
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})

#This function is for logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#This function is for add_data
def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = HabitForm(request.POST)
            if fm.is_valid():
                    messages.success(request,"Data Added Successfully!")
                    profile = fm.save(commit=False)
                    profile.user = request.user
                    profile.save()
                    return redirect('/add')
        else:
            fm = HabitForm()
        return render(request, 'add.html', {'form': fm, 'fname': request.user.first_name, 'lname': request.user.last_name})
    else:
        return HttpResponseRedirect('/login/')

#This function is to show data
def show(request):
    if request.user.is_authenticated:
        data = HabitModel.objects.all()
        user = request.user
        return render(request,'show.html',{'user':user,'data':data})
    else:
        return HttpResponseRedirect('/login/')


#This function is to show the profile
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        data = HabitModel.objects.filter(user=user)
        # phone = UserphoneModel.objects.all()
        return render(request,'profile.html',{'data':data,'fname': request.user.first_name,'email':request.user.email,'phone':request.user.last_name})
    else:
        return HttpResponseRedirect('/login/')

#This function is to show Home Page
def home(request):
    if request.user.is_authenticated:
        data = HabitModel.objects.all()
        return render(request,'homepage.html',{'data':data})
    else:
        return HttpResponseRedirect('/login/')

#This function is to show the very first page
def first_page(request):
    return render(request,'first_page.html')