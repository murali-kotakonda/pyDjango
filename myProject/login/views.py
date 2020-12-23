from django.shortcuts import render
from django.http import HttpResponse

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from .forms import UserForm, PersonForm
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

"""
How to capture the request data from the web page.

Req:
There is a form that has name and age
customer enters data for name and age
in the views.py we need to capture the name and age from the request page
views.py has to send the name , age to the response page.

"""
#method to show the request page GET
def handleRequest1(request):
    return render(request, "request1.html")


#method when customer clicks on "requestPost" click
def handlePostRequest(request):
    return render(request, "requestPost.html")




"""
How to get the request data in th views.py:
-------------------------------------------------
req page has below fields:
------------------------------

in request1.html:
--------------------
 <td><input type="text" name="name" /></td>
  <td><input type="text" name="age"/></td>

To capture name and age in view.py provide below code:
name= request.GET["name"]  # to get the name
age = int(request.GET["age"])  # to get the age

the field name should be used in the views.py to capture the request.

 
  
In views:
---------------
For GET Calls: [IN REQUEST PAGE <form action="/login/submit1">]
How to get the name? 
userName= request.GET["name"]  # get the field value using the field name

How to get the age?
userAge = int(request.GET["age"]) # get the field value using the field name


For POST Calls:[IN REQUEST PAGE <form action="/login/submit1" method ="post">]
How to get the name?
userName= request.POST["name"]  # get the field value using the field name

How to get the age?
userAge = int(request.POST["age"]) # get the field value using the field name



"""

#method to handle when data is submitted from request1.html
def handleSubmit1(request):
        name= request.GET["name"]
        age = int(request.GET["age"])
        return render(request, "showRes8.html", {"msg" : "hi from GET " ,"myName" : name , "myAge" : age})


def handleSubmitPost(request):
    name = request.POST["name"]
    age = int(request.POST["age"])
    return render(request, "showRes8.html", {"msg": "hi from POST ", "myName": name, "myAge": age})



"""
How to identify in the views.py whether the request iS GET or POST?
use check

if(request.method == 'GET'):
  <WRITE HANDLING FOR GET>

if(request.method == 'POST'):
  <WRITE HANDLING FOR POST>

The request page contains two forms:
- GET form with button
- Post form with button

and url is same for both the forms

when customer clicks on any button the call with happen to the one method in views.py

"""


#method when customer clicks on "GetAndPost" click
def showRequestGetAndPost(request):
    return render(request, "requestGetAndPost.html")

#handle both post and get when customer clicks on Button
def handleRequestGetAndPost(request):
    if(request.method == 'GET'):
        name= request.GET["name"]
        age = int(request.GET["age"])
        return render(request, "showRes8.html", {"msg" : "hi from GET " ,"myName" : name , "myAge" : age})

    if (request.method == 'POST'):
        name = request.POST["name"]
        age = int(request.POST["age"])
        return render(request, "showRes8.html", {"msg" : "hi from POST " ,"myName": name, "myAge": age})


"""
Get Method vs Post method:
----------------------------
For a GET Call, the data submitted by the customer is appended to the url and is visible in the URL.
input data is part of request URL.
http://127.0.0.1:8000/login/submit1/?name=prasanna&age=25
Base_url + resource_url + Query params [ after ? what ever that comes ]

Base_url : http://127.0.0.1:8000/login/
resource_url :submit1
Query params : name=prasanna&age=25

Every query param is seperated by  & 
For generic data submission use GET call.
CANNOT USE FOR SENSITIVE DATA SUBMISISON.
Cannot handle large data. 
All the link calls aRe get calls


Button call can be either get or post call


For a  post call, the data submitted by customer is not appended to URL , 
input data is part of request body.
EX:  http://127.0.0.1:8000/login/submit1
For secure data transfer use POST call. 
Can handle large data.
File uploads/image  upoad should be done using post calls.




Diff between link and button?
-------------------------------------
syntax for link:
Case#1:
<a href="/login/ex1">Ex1</a> &nbsp;&nbsp;&nbsp;

If customer clicks on link then call will hapen as : 
URL : http://127.0.0.1:8000/login/ex1
HTTP METHOD: GET
For a link the navigation is specified using "href" attribute.

syntax for button:
Case#2
<form action= "/login/register/">


  <input id="submit" type="submit" value="Login"/></td>
</form>
If customer clicks on BUTTON then call will hapen as : 
URL : http://127.0.0.1:8000/login/register/
HTTP METHOD: GET
For a button the navigation is specified using <form> action 

Case#3
<form action= "/login/register2/" method="post">


  <input id="submit" type="submit" value="Login"/></td>
</form>
If customer clicks on BUTTON then call will hapen as : 
URL : http://127.0.0.1:8000/login/register2/
HTTP METHOD: post
For a button the navigation is specified using <form> action 

In a form
<form action= "/login/register2/" method="post">
action specifies the URL
method specifies the HTTP method 
ex : method="post"
     method="get"
    

"""


"""
How to show the menu for all pages?
How to reuse the html in other htmls?

use:
{% include "index.html" %}


"""
#response the input2
def handleRequest2(request):
    return render(request, "request2.html", {"status": 1})

"""
Need a form that takes input for below fields:

firstname
lastname
sem
branch

-> submit form data
-> validate the data
-> firstname min 8 chars max 15
-> lastname is optional
-> sem is  anum only [1-8] allowed
-> for branch  only ("csc", "ece", "mech" , "civil")

-> if validaation is succss -> Data saved
-> if valdiation is failed->show error message + data retaied using studentForm.html



"""
def handleSubmit2(request):
    if(request.method == 'GET'):
        firstname= request.GET["firstname"]
        lastname = request.GET["lastname"]
        sem = int(request.GET["sem"])
        branch = request.GET["branch"]
        return render(request, "showRes9.html", {"msg" : "hi from GET " ,"myFirstName" : firstname , "myLastName" : lastname, "mySem": sem, "myBranch": branch})

"""
Req:
->show Login page:
a)Loginname
b)password

customer fills the form and click on "login" button.


if loginname value is "admin" and password value is "admin" show Login succes
if not show "login failure"

"""

#response the input3
def showLogin(request):
    return render(request, "login.html")


"""
for post calls in the html pass csrf_token info:
-------------------------------
 {% csrf_token %}
 
"""
def handleLogin(request):
    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]
        if username=='admin'and password=='admin@123':
            return render (request,"showLoginResponse.html",{"msg" :" login sucess"})
        else:
            return render(request, "showLoginResponse.html", {"msg": " login failure"})

"""
"""

class RegisterInfo:

    def __init__(self,firstname,lastname,age,username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.username = username
        self.password = password

"""
Requirement:
->Take input for firstname,lastname,age,username,password.
->validate the data
firstname has to be min 8 char
lastname has to be min 6 char
age has to be in 18-60
username has to be min 5 char
password has to be in  8-12 char
-> if valdiation success show "Registration success"
-> if valdiation failed show error message and retain the data

 
How to retian the data in html:
---------------------------------------------------
from the views.py we need to send the object to the html

we have written in the html 
value="{{info.username}}"
value="{{info.firstname}}"
value="{{info.lastname}}"
value="{{info.age}}"

to retain the data in the 'register.html'.
 

"""
#response the input4
def handleRegister(request):
    if (request.method == 'GET'):
            # when  customer clicks on register link
            return render(request, "register.html", {})

    if (request.method == 'POST'):
        # when  customer clicks on register button
        #capture the request data
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]

        #keep the data in RegisterInfo object
        info = RegisterInfo(firstname,lastname,age,username,password)

        # in the request data is wrong then send erorr message and info object to the register.html

        if len(firstname) < 8:
            return render(request, "register.html", {"msg": " firstname has to be min 8 char","info":info})
        if len(lastname) < 6:
            return render(request, "register.html", {"msg": " lastname has to be min 6 char","info":info})
        if (age) not in  range(18,60):
            return render(request, "register.html", {"msg": " age has to be in 18-60","info":info})
        if len(username) < 5:
            return render(request, "register.html", {"msg": " username has to be min 5 char","info":info})
        if len(password) not in range (8,12) :
            return render(request, "register.html", {"msg": " password has to be in  8-12 char","info":info})

        return render(request, "success.html", {"msg": " Registration sucess...."})
    return HttpResponse("matching handler not found")


"""
Requirement:
->Take input for firstname,lastname,age,username,password.
->validate the data
firstname has to be min 8 char
lastname has to be min 6 char
age has to be in 18-60
username has to be min 5 char
password has to be in  8-12 char
-> if valdiation success show "Registration success"
-> if valdiation failed show error message and retain the data


Show all the error messages and retain the data.


"""

def handleRegister2(request):
    if (request.method == 'GET'):
            # when  customer clicks on register link
            return render(request, "register2.html", {})

    if (request.method == 'POST'):
        # when  customer clicks on register button
        #capture the request data
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]

        #keep the data in RegisterInfo object
        info = RegisterInfo(firstname,lastname,age,username,password)

        # in the request data is wrong then send erorr message and info object to the register.html
        errors = []
        if len(firstname) < 8:
            errors.append(" firstname has to be min 8 char.")

        if len(lastname) < 6:
            errors.append(" lastname has to be min 6 char.")

        if (age) not in  range(18,60):
            errors.append(" age has to be in 18-60.")

        if len(username) < 5:
            errors.append(" username has to be min 5 char.")

        if len(password) not in range (8,12) :
            errors.append(" password has to be in  8-12 char.")

        if len(errors) == 0:
            return render(request, "register2.html", {"errors": errors,"info":info})

        return render(request, "success.html", {"msg": " Registration sucess...."})
    return HttpResponse("matching handler not found")

#for the reuse method
def handleReuse(request):
    return render(request, "Reuse.html", {"data": "hi man "})


"""
-> it is often difficult to capture the request data when we have multiple incoming data.
ex: if the formhas 20 fields , then we nee dto write 20 line sof code for requets capturing.

problem:
code repeation

solution:
->use model forms
-> django will capture the request data and provides in the form of object
-> also django generates the form in the html
-> code simpification


Requirement:
1.Capture fname,lname,address,email 
and perform Request capturing.


the  following code  in the form1.html generates the form automatically.
- {{ form }}
- {{ form.as_table}}
- {{ form.as_p}}
- {{ form.as_ul}}


"""
def handleForm1(request):
    form= UserForm()
    return render(request, "form1.html", {"form":form})
"""
for the text field use forms.CharField
for the email field use forms.EmailField


There 2 situations: using basic Form (forms.Form) and ModelForm (forms.ModelForm).

If you are using a ModelForm then there is no any need of playing with a cleaned_data dictionary 
because when you do form.save() it is already be matched and the clean data is saved. But you are using basic Form then you have to manually match each cleaned_data to its database place and then save the instance to the database not the form.

For example basic Form:

if form.is_valid():
    ex = Example()
    ex.username = form.cleaned_data['username']
    ex.save()
For example ModelForm:

if form.is_valid():
    form.save()

"""
def handleForm2(request):
    if (request.method == 'GET'):
        form = UserForm()
        return render(request, "form1.html", {"form": form})

    if (request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            return render(request, "response1.html",{"fname": fname, "lname": lname, "address":address , "email": email})  # htmls reusability
        else:
            return render(request, "form1.html", {"form": form})




#pdf download
#$ python -m pip install reportlab
"""
as the req is to generate and download the pdf.
we need to change the response properties.
view method rerturns the response object.

-> use reportlab canvas for generating the pdf.
Provide
-> Content-Disposition  as 'attachment; filename="file.pdf'

using the "p = canvas.Canvas(response)" associate the pdf with response obj
"""

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

"""

for working with csv , use import csv module.
as the req is to generate and download the csv.
we need to change the response properties.
view method rerturns the response object.



-> Provide
Content-Disposition  as 'attachment; filename="emps.csv'
content_type      'text/csv'

-> associate the csv with response obj  using
writer = csv.writer(response)


"""
def getCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emps.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'age','sal'])
    writer.writerow(['101', 'user1', 28, 1000])
    writer.writerow(['102', 'user2', 29, 1200])
    writer.writerow(['103', 'user3', 30, 1300])

    return response


"""
Cookie : HTTP cookies are used to identify specific users and improve your web browsing experience
cookie info is saved in the local client system and ofen used for client identification.

Every request will carry the cookie to the backend

How to set the cookies in the response obj in views.py:
---------------------------------------
response.set_cookie('MyCookie', 'KRISHNA DJANGO')
# here 'MyCookie' is cookie name and 'KRISHNA DJANGO' is the cookie value




How to get the cookies from web page?
-------------------------------------------
myCookie  = request.COOKIES['MyCookie']
or
myCookie  = request.COOKIES.get('MyCookie')
 


"""


# method will set the cookie ad add cookie to response
def handleSetCookie(request):
    response = HttpResponse("Added cookie")
    response.set_cookie('MyCookie', 'KRISHNA DJANGO')
    return response

# method to get the cookie value from the request
def handleGetCookie(request):
    myCookie  = request.COOKIES['MyCookie']
    if myCookie:
        return HttpResponse("showing cookie COOKIE VALUE =  "+  myCookie)
    else:
        return HttpResponse("cookie COOKIE " + myCookie + " not found.")

def handleDeleteCookie(request):
        #response = HttpResponseRedirect('/url/to_your_login')
        response = HttpResponse("deleted cookie")
        response.delete_cookie('MyCookie')
        return response


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

"""
Table relationships:
------------------
-> One to One
One row in tabel-1 is related to one row in table-2

-> One to Many
One row in tabel-1 is related to multiple rows in table-2

-> Many to One
many rows in tabel-1 is related to one row in table-2

-> Many to Many
many rows in tabel-1 is related to many rows in table-2


One to One:
--------------

Req:
One Employee has one address

How many tables?
ans)Two tables


1.Address Table
id    ( PK)       -> NOT NULL and unique
street
city
country 



2.Employee table
ID     ( PK)       -> NOT NULL and unique
firstname
lastname
currAddr  (FK)    -> Refers to the id column of Address Table



Address:
-----------------------
id  street     city   country     zip
100   abc      hyd     in        7676
200   abc1     che     in        7677
300   abc2     mum     in        7678
400   abc3     bang    in        7679


Employee:
---------------------
id  firstname lastname  currAddr
10   user1     kumar1      100 
20   user2     kumar2      200
30   user3     kumar3      300
40   user4     kumar4      400


1.Display employee
select * from Employee

2.Display employee with address?
[use joins]
select e.id, e.firstname , e.lastname ,a.street ,a.city, a.country, a.zip
from Employee e , Address a
where e.id = a.id

  
"""
def handleOnetoone(request):
    a= Addr(street="marath" ,city= "bang" , country ="india", zip="1234")
    a.save()

    e= Emp(firstName="kumar",lastName="ram" , currAddr=a)
    e.save()
    return HttpResponse("one to one success")



def handleManytoone(request):
    #create  cust obj and save
    c= Customer(name="ramana" , age=34)
    c.save()

    # create mul accounts obj
    #every account has customer associated
    # and save every account
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

   # c1.save()

    c1.students.add(s1)
    c1.students.add(s2)

    c1.save()
    return HttpResponse(" many to many success")