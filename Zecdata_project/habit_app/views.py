from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import signupForm,HabitForm
from .models import HabitModel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

#This function is for signup_form
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import signupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def sign_up(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            text_content = strip_tags(message)
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                mail_subject, message, to=[to_email]
            )
            email.attach_alternative(message, "text/html")
            email.send()
            messages.success(request, "Verify your email address to Login!")
            return redirect('login')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.warning(request, "Email verified now you can login!")
        return redirect('login')
    else:
        return HttpResponse('Activation link is Expired!')



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