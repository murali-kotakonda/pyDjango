from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
import csv

# Create your views here
def handleMenu(request):
    return render(request, "studentMenu.html", {})

def handleCreate(request):
    e = Student(firstName='ram', lastName='kumar', age=24, username="admin", password="admin")
    e.save()
    return render(request, "showStudent.html", {"msg": "student created"})

def handleCreate1(request):
    if (request.method == 'GET'):
        return render(request, "student.html",{})

    if (request.method == 'POST'):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]


        if len(firstname) < 8:
            return render(request, "student.html", {"msg": " firstname has to be min 8 char","firstname":firstname})
        if len(lastname) < 6:
            return render(request, "student.html", {"msg": " lastname has to be min 6 char","lastname":lastname})
        if (age) not in  range(18,60):
            return render(request, "student.html", {"msg": " age has to be in 18-60","age":age})
        if len(username) < 5:
            return render(request, "student.html", {"msg": " username has to be min 5 char","username":username})
        if len(password) not in range (8,12) :
            return render(request, "student.html", {"msg": " password has to be in  8-12 ch","password":password})

        s = Student(firstName=firstname, lastName=lastname, age=age, username=username, password=password)
        s.save()

        return render(request, "showStudent1.html", {"msg": "Student created"})


#search by ID
def handleGet(request):
    if (request.method == 'GET'):
        return render(request, "get.html",{})

    if (request.method == 'POST'):
        MyId = int(request.POST["id"])
        sObj=None

        try:
         sObj = Student.objects.get(id=MyId)

        except:
         return render(request, "get.html", {"msg":"invalid id"})

        else:
         return render(request, "showGet.html", {"Student":sObj})

#search by Username
def handleGet1(request):
    if (request.method == 'GET'):
        return render(request, "get1.html",{})

    if (request.method == 'POST'):
        MyName = (request.POST['username'])
        sObj=None

        try:
         sObj = Student.objects.get(username=MyName)

        except:
         return render(request, "get1.html", {"msg":"invalid name"})

        else:
         return render(request, "showGet.html", {"Student":sObj})

#delete by ID
def handleDlt(request):
    if (request.method == 'GET'):
        return render(request, "dlt.html",{})

    if (request.method == 'POST'):
        MyId = int(request.POST["id"])
        sObj=None
        try:
            sObj = Student.objects.get(id=MyId)
            sObj.delete()
        except:
            return render(request, "get.html", {"msg":"invalid id"})
        else:
            return render(request, "showDlt.html", {"msg" :"delete success"})
#get all Student
def handleGetall(request):
    if (request.method == 'GET'):
        list=Student.objects.all()
        return render(request, "getall.html", {"Student": list})

#update by id
def handleUpdate(request):
        MyId = int(request.GET["id"])
        sObj = Student.objects.get(id=MyId)
        return render(request, "update.html", {"Student":sObj})

def handleUpdate1(request):
        #capture the incoming data
        id = request.POST["id"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]

        #get existing data from db
        sObj = Student.objects.get(id=id)
        sObj.firstName = firstname
        sObj.lastName = lastname
        sObj.age = age
        sObj.username = username


        if len(firstname) < 8:
            return render(request, "update.html", {"msg": " firstname has to be min 8 char","Student":sObj})
        if len(lastname) < 6:
            return render(request, "update.html", {"msg": " lastname has to be min 6 char","Student":sObj})
        if (age) not in  range(18,60):
            return render(request, "update.html", {"msg": " age has to be in 18-60","Student":sObj})
        if len(username) < 5:
            return render(request, "update.html", {"msg": " username has to be min 5 char","Student":sObj})

        sObj.save()

        return render(request, "showStudent1.html", {"msg": "Student updated"})

def handleLogin(request):
    if (request.method == 'GET'):
        return render(request, "login.html", {})
    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]

        sObj = None

        try:
            sObj = Student.objects.filter(username=username,password=password)
        except:
            return render(request, "login.html", {"msg": "invalid username or password"})

        if (sObj):
            s=sObj.first()
            request.session["id"]=s.id
            request.session["fname"] = s.firstName
            request.session["lname"] = s.lastName
            return render(request, "studentMenu.html", {"msg": "login sucess"})
        else:
            return render(request, "login.html", {"msg": "invalid username or password"})

def handleLogout(request):
    if (request.method == 'GET'):
        del request.session["id"]
        del request.session["fname"]
        del request.session["lname"]
        return render(request, "login.html", {"msg": "logout sucess"})

def getCsv(request):
    response = HttpResponse(content_type='text/csv')

