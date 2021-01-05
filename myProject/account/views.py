from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here
from .forms import UserRegistrationForm
from .permission import user_email_valid


def handleIndex(request):
    #if request.user.is_authenticated:
     #   return render(request, 'showAccount.html')
    return render(request, "accountHome.html", {})

"""
username should be unique:
emial should be unique
provide confirm password filed
password and confirm password should be same

show errror messages when data is invalid
when Registration is success show Registration success
when Registration is failed show Registration failed with erorr messages

"""
#if request.user.is_authenticated:
#       return render(request, 'showAccount.html')
def handleRegisterAccount(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            #password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            """
            if password1 != password2:
                check1 = True
                messages.error(request, 'Password doesn\'t matched',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            """
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
                #return redirect('accounts:register')
                return render(request, 'accountRegister.html')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name= firstName , last_name=lastName)
                messages.success(
                    request, f'Thanks for registering {user.username}!', extra_tags='alert alert-success alert-dismissible fade show')
                #return redirect('accounts:login')
                return render(request, 'accountLogin.html')

    else:
        form = UserRegistrationForm()
    return render(request, 'accountRegister.html', {'form': form})

"""
Session handling:
--------------------
- use inbuilt decorator provided by django

write "@login_required" before the funtion 

login_required expected the login_url 
if session is inactive/logout then the page is redirected to the login_url.
ex: 

@login_required(login_url="/account/accountLogin")
def handleShowMyAccount(request):
  #some code
    
"""


@login_required(login_url="/account/accountLogin")
def handleAccountLogout(request):
    logout(request)
    form = UserRegistrationForm()
    return render(request, 'accountRegister.html', {'form': form})


 #if request.user.is_authenticated:
#   return render(request, 'showAccount.html')

def handleAccountLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            #redirect_url = request.GET.get('next', 'home')
            #return redirect(redirect_url)
            request.session["userName"] = username
            return render(request, 'showAccount.html',{'user':user})
        else:
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'accountLogin.html')

@login_required(login_url="/account/accountLogin")
def handleShowMyAccount(request):
    userName = request.session["userName"]
    user = User.objects.get(username =userName)
    print(user.id,user.username)
    return render(request, 'showAccount.html', {"user": user})



"""


"""

def email_check(user):
    return user.email.endswith('com')

@login_required(login_url="/account/accountLogin")
#@user_passes_test(email_check,login_url="/account/accountLogin")
#@user_passes_test(lambda user: user.is_staff)
#@user_passes_test(lambda user: user.is_authenticated)
@user_email_valid
def handleGetAccount(request):
    if (request.method == 'GET'):
        # click on link
        return render(request, "accountSearch.html", {})
    if (request.method == 'POST'):
        # click on serach button
        name =  request.POST["name"]

        # select * from customer where id = <id>
        try:
            eObj = User.objects.get(username=name)
        except:
            return render(request, "accountSearch.html", {"msg": "invalid userName"})
        else:
            return render(request, "accountSearchResult.html", {"user": eObj})

