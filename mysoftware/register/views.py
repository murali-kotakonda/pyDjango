from django.shortcuts import render
from django.http import HttpResponse
from register.forms import PersonForm
from .models import Person

# Create your views here.
def handleIndex(request):
    return render(request, "index.html", )



def handlePerson(request):
    if request.method == "GET":
        form = PersonForm()
        return render(request, 'personForm1.html', {'form': form})
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'personForm2.html', {'form': form,'msg':'registration success'})
        else:
            return render(request, 'personForm1.html', {'msg': "reg failure"})

def handleLogin(request):
    if (request.method == 'GET'):
        return render(request, "index.html", {})

    if (request.method == 'POST'):
        userName = request.POST["username"]
        password = request.POST["password"]

        print("username="+userName+"password="+password)
        pObj = None

        try:
            pObj = Person.objects.filter(userName=userName,password=password)
            print("hello")
        except Exception as ex:

            print("hi...",ex)
            return render(request, "index.html", {"msg": "invalid username or password"})

        if (pObj):
            print("hiiiiii...")
            p=pObj.first()
            request.session["id"]=p.id
            request.session["fname"] = p.firstName
            request.session["lname"] = p.lastName
            return render(request, "index1.html", {"msg": "login sucess"})
        else:
            return render(request, "index.html", {"msg": "invalid username or password"})

def handleMyProfile(request):
    MyId = int(request.session["id"])
    pObj = Person.objects.get(id=MyId)
    return render(request, "showProfile.html", {"p": pObj})

def handleUpdate(request):
     MyId = int(request.GET["id"])
     pObj = Person.objects.get(id=MyId)
     return render(request, "update.html", {"Person": pObj})


def handleUpdate1(request):
    # capture the incoming data
    id = request.POST["id"]
    firstName = request.POST["firstname"]
    lastName = request.POST["lastname"]
    age = int(request.POST["age"])
    email = request.POST["email"]
    userName = request.POST["username"]

    # get existing data from db
    pObj =Person.objects.get(id=id)
    pObj.firstName = firstName
    pObj.lastName = lastName
    pObj.age = age
    pObj.email = email
    pObj.userName = userName

    if len(firstName) > 8:
        return render(request, "update.html", {"msg": " firstname is no more than 8 char", "Person": pObj})
    if len(lastName) > 6:
        return render(request, "update.html", {"msg": " lastname is no more than 6 char", "Person": pObj})
    if (age) not in range(18, 60):
        return render(request, "update.html", {"msg": " age has to be in 18-60","Person": pObj})
    if len(email) > 10:
        return render(request, "update.html", {"msg": " email is no more than 5 char","Person": pObj})
    if len(userName) > 5:
        return render(request, "update.html", {"msg": " username is no more than 5 char","Person": pObj})

    pObj.save()

    return render(request, "showPerson.html", {"msg": "Person updated"})


def handleLogout(request):
    if (request.method == 'GET'):
        del request.session["id"]
        del request.session["fname"]
        del request.session["lname"]
        return render(request, "index.html", {"msg": "logout sucess"})


