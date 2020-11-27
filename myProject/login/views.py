from django.shortcuts import render
from django.http import HttpResponse
from login.forms import UserForm,PersonForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Addr,Emp
from .models import Customer,Account
from .models import Student,Course


import csv



# Create your views here.
class Person:
    id=None
    name=None
    age= None
    pancard=None

class StudentInfo:
    firstName = None
    lastName = None
    addr = None

class Address:
    hno= None
    city= None
    state= None
    country= None
    pin = None

class Employee:
    id=None
    name=None
    age= None
    pancard=None

def ex1(request):
    res = "<font color='red'>welcome to django</font>"
    return HttpResponse(res)

def handleHello(request):
    return render(request, "helloResponse.html", {})

def process(request):
    return render(request, "process.html", {})

def handleResponseData(request):
    return render(request, "showResponse.html", {"data":"hi How Are You "})
#here we are sending the response
# response param name: data
# response param value: hi How Are You
#Response data is deligated to showResponse.html uisng dictionary.



def handleMultipleResponse(request):
    responseData = {"name":"hero","id":101,"salary":23900.089}
    return render(request, "showMultiResponse.html", responseData)


#handleShow1 has to send the person object to the "showRes1.html"
#for one personal object

def handleShow1(request):
    p = Person()
    p.id=2000
    p.name="kumar"
    p.age=34
    p.pancard="CNVPD2557D"
    return render(request, "showRes1.html", {"pData": p})

#for person with adress object
"""
Req:
Student class is related with Address class using "has a" .
Student obj internally has address Obj.

send student object from backend to template(html)

steps:
create Address obj with data
create StudentInfo obj with data
keep Address obj inside the StudentInfo obj
Send StudentInfo obj  to the "showRes2.html".
showRes2.html :-> print both StudentInfo and Address
"""
def handleShow2(request):
    #create student obj
    stu= StudentInfo()
    stu.firstName="ram"
    stu.lastName="sharma"

    #create address obj
    a = Address()
    a.hno ="#23"
    a.city="hyd"
    a.state="KA"
    a.country ="IN"
    a.pin = 1234

    #keep address obj inside student
    stu.addr =a

    return render(request, "showRes2.html", {"sObj": stu})

#lists of strings
"""
Req:
Send list of strings to the template.


jinja code in python:
-----------------------
 use {%   <python code>  %} i html to write the python code.
 
 
{{forloop.counter }}   -> to disply the counter
{{forloop.first}}      -> boolean inform whether element is in 1st position
{{forloop.last}}  -> boolean inform whether element is in last position


{% for city in names %}  -> for starts

{% endfor %}-> for loop ends

No indentation in html

"""
def handleShow3(request):
    myCities = ["hyd","bangalore","chennai","kolkatta","pune","maduari"]
    return render(request, "showRes3.html", {"cities": myCities})

#for employee object
def handleShow4(request):
    p = Person()
    p.id = 2000
    p.name = "kumar"
    p.age = 34
    p.pancard = "CNVPD2557D"

    e = Employee()
    e.id=7890
    e.name="Dash"
    e.age=56
    e.pancard="CND"
    return render(request, "showRes4.html",{"pData": p ,"eData": e})

"""
Req:
Send list of Person objs to the template.

handleShow5 has to return the list of person obj to the "showRes5.html" 
"""
#lists of persons
def handleShow5(request):
    p1 = Person()
    p1.id = 2000
    p1.name = "kumar"
    p1.age = 34

    p2 = Person()
    p2.id = 2001
    p2.name = "ram"
    p2.age = 35

    list = [p1,p2] # add p1,p2 to the list
    return render(request, "showRes5.html", {"persons": list})

"""
Req:
Send list of Student with address objs to the template.
every Student obj has address obj.

if there are no studnts then display :-> "No students "
if there is no address for studnt then display :-> "No address available "


"""
#lists of students
def handleShow6(request):
    stu1 = Student()
    stu1.firstName = "ram"
    stu1.lastName = "sharma"

    a1 = Address()
    a1.hno = "#23"
    a1.city ="hyd"
    a1.state = "ka"
    a1.country = "IN"
    a1.pin = 1234

    stu1.addr =a1

    stu2 = Student()
    stu2.firstName = "Hari"
    stu2.lastName = "Mishra"

    a2 = Address()
    a2.hno = "#12"
    a2.city = "bgl"
    a2.state = "jk"
    a2.country = "USA"
    a2.pin = 4567

    stu2.addr = a2

    list = []
    list.append(stu1)
    list.append(stu2)
    return render(request, "showRes6.html", {"students": list})


#index every url

def handleIndex(request):
    return render(request, "index.html", )

"""
Req:
How to write the if statements in the Html.

if the view sends "1" to the html, then html has to print "SUCCESS"
if the view sends "0" to the html, then html has to print "FAILURE"
"""
#1=sucess or failure
def handleShow7(request):
    return render(request, "showRes7.html",{"status":0})

#response the input
def handleRequest1(request):
    return render(request, "request1.html", {"status": 1})


def handleSubmit1(request):
    if(request.method == 'GET'):
        name= request.GET["name"]
        age = int(request.GET["age"])
        return render(request, "showRes8.html", {"msg" : "hi from GET " ,"myName" : name , "myAge" : age})

    if (request.method == 'POST'):
        name = request.POST["name"]
        age = int(request.POST["age"])
        return render(request, "showRes8.html", {"msg" : "hi from POST " ,"myName": name, "myAge": age})


#response the input2
def handleRequest2(request):
    return render(request, "request2.html", {"status": 1})

def handleSubmit2(request):
    if(request.method == 'GET'):
        firstname= request.GET["firstname"]
        lastname = request.GET["lastname"]
        sem = int(request.GET["sem"])
        branch = request.GET["branch"]
        return render(request, "showRes9.html", {"msg" : "hi from GET " ,"myFirstName" : firstname , "myLastName" : lastname, "mySem": sem, "myBranch": branch})

   #response the input3
def handleRequest3(request):
    return render(request, "request3.html", {"status": 1})

def handleSubmit3(request):
    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]
        if username=='admin'and password=='admin@123':
            return render (request,"showRes10.html",{"msg" :" login sucess"})
        else:
            return render(request, "showRes10.html", {"msg": " login failure"})


#response the input4
def handleRegister(request):
    if (request.method == 'GET'):
        return render(request, "register.html",{})

    if (request.method == 'POST'):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]

        if len(firstname) < 8:
            return render(request, "register.html", {"msg": " firstname has to be min 8 char","firstname":firstname})
        if len(lastname) < 6:
            return render(request, "register.html", {"msg": " lastname has to be min 6 char","lastname":lastname})
        if (age) not in  range(18,60):
            return render(request, "register.html", {"msg": " age has to be in 18-60","age":age})
        if len(username) < 5:
            return render(request, "register.html", {"msg": " username has to be min 5 char","username":username})
        if len(password) not in range (8,12) :
            return render(request, "register.html", {"msg": " password has to be in  8-12 char","password":password})

        return render(request, "sucess.html", {"msg": " Registation sucess...."})


#for the reuse method
def handleReuse(request):
    return render(request, "Reuse.html", {"data": "hi man "})

def handleForm1(request):
    form= UserForm()
    return render(request, "form1.html", {"form":form})


def handleProcessForm1(request):
    form = UserForm(request.POST)


def handleForm2(request):
    if (request.method == 'GET'):
        form = UserForm()
        return render(request, "form2.html", {"form": form})

    if (request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            return render(request, "response1.html",{"fname": fname, "lname": lname, "address":address , "email": email})  # htmls reusability
        else:
            return render(request, "form2.html", {"form": form})  # htmls reusability


#pdf download
def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 26)
    p.drawString(100,700, "Hello user this is your statement")
    p.drawString(200,900, "see you soon.....")
    p.showPage()
    p.save()
    return response

#csv download
def getCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emps.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'age','sal'])
    writer.writerow(['101', 'user1', 28, 1000])
    writer.writerow(['102', 'user2', 29, 1200])
    writer.writerow(['103', 'user3', 30, 1300])

    return response
#cookies response
def handleSetCookie(request):
    response = HttpResponse("Added cookie")
    response.set_cookie('MNPCOOKIE', 'KRISHNA DJANGO')
    return response

def handleGetCookie(request):
    v  = request.COOKIES['MNPCOOKIE']
    return HttpResponse("showing cookie COOKIE VALUE =  "+  v);


def handlePerson(request):
    if request.method == "GET":
        form = PersonForm()
        return render(request, 'personForm1.html', {'form': form})
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'personForm2.html', {'form': form})
        else:
            form = PersonForm()
            return render(request, 'personForm1.html', {'form': form})


def handleOnetoone(request):
    a= Addr(street="marath" ,city= "bang" , country ="india", zip="1234")
    a.save()

    e= Emp(firstName="kumar",lastName="ram" , currAddr=a)
    e.save()
    return HttpResponse("one to one success")



def handleManytoone(request):
    c= Customer(name="ramana" , age=34)
    c.save()

    a1 = Account(name="loan account", custId = c)
    a2 = Account(name="credit account", custId=c)
    a3 = Account(name="debit account", custId=c)
    a1.save()
    a2.save()
    a3.save()

    return HttpResponse("one to many/many to one success")


def handleManytomany(request):
    s1 = Student()
    s1.name = "kumar"
    s1.mobileNo = "1223434"
    s1.save()

    s2 = Student()
    s2.name = "kumar1"
    s2.mobileNo = "999999"
    s2.save()

    c1 = Course()
    c1.courseName = "django"

    c1.save()

    c1.students.add(s1)
    c1.students.add(s2)

    c1.save()
    return HttpResponse(" many to many success")