

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here
from .permission import is_session_active


def handleMenu(request):
    return render(request, "customerMenu.html", {})


def handleCreate(request):
    e = Employee(firstName='ram', lastName='kumar', age=24, username="admin", password="admin")
    e.save()
    return render(request, "showEmployee.html", {"msg": "emp created"})


def handleCreate1(request):
    if (request.method == 'GET'):
        return render(request, "employee.html",{})

    if (request.method == 'POST'):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]


        if len(firstname) < 8:
            return render(request, "employee.html", {"msg": " firstname has to be min 8 char","firstname":firstname})
        if len(lastname) < 6:
            return render(request, "employee.html", {"msg": " lastname has to be min 6 char","lastname":lastname})
        if (age) not in  range(18,60):
            return render(request, "employee.html", {"msg": " age has to be in 18-60","age":age})
        if len(username) < 5:
            return render(request, "employee.html", {"msg": " username has to be min 5 char","username":username})
        if len(password) not in range (8,12) :
            return render(request, "employee.html", {"msg": " password has to be in  8-12 ch","password":password})

        e = Employee(firstName=firstname, lastName=lastname, age=age, username=username, password=password)
        e.save()

        return render(request, "showEmployee1.html", {"msg": "emp created"})


#search by ID
@is_session_active
def handleGet(request):
    if (request.method == 'GET'):
        # click on link
        return render(request, "get.html", {})
    if (request.method == 'POST'):
        # click on serach button
        MyId = int(request.POST["id"])

        # select * from customer where id = <id>
        try:
            eObj = Employee.objects.get(id=MyId)
        except:
            return render(request, "get.html", {"msg": "invalid id"})
        else:
            return render(request, "showGet.html", {"Employee": eObj})


#search by Username
@is_session_active
def handleGet1(request):
    if (request.method == 'GET'):
        return render(request, "get1.html",{})

    if (request.method == 'POST'):
        MyName = (request.POST['username'])
        eObj=None

        try:
         eObj = Employee.objects.get(username=MyName)

        except:
         return render(request, "get1.html", {"msg":"invalid name"})

        else:
         return render(request, "showGet.html", {"Employee":eObj})

#delete by ID
@is_session_active
def handleDlt(request):
    if (request.method == 'GET'):
        return render(request, "dlt.html",{})

    if (request.method == 'POST'):
        MyId = int(request.POST["id"])
        eObj=None
        try:
            eObj = Employee.objects.get(id=MyId)
            eObj.delete()
        except:
            return render(request, "get.html", {"msg":"invalid id"})
        else:
            return render(request, "showDlt.html", {"msg" :"delete success"})

"""
URL rewriting:
-----------------------
 <a href="/customer/editEmployee?id={{e.id}}">Edit</a>
  <a href="/customer/dltemp?id={{e.id}}">Delete</a>
  
  along with the url we are appending the data
  ex: 
  /editEmployee?id={{e.id}}
  /dltemp?id={{e.id}
  
  what ever that comes after the "?" is the request param info added to the url
"""
#get all employee
@is_session_active
def handleGetall(request):
	#select * from customer
    list=Employee.objects.all()
    # all rows are converted to emp objects
    # al emp objs are stored in list
    return render(request, "getall.html", {"emps": list})

#update by id
@is_session_active
def handleUpdate(request):
        MyId = int(request.GET["id"])
        eObj = Employee.objects.get(id=MyId)
        return render(request, "update.html", {"Employee":eObj})

@is_session_active
def handleUpdate1(request):
        #capture the incoming data
        id = request.POST["id"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]

        #get existing data from db
        eObj = Employee.objects.get(id=id)
        eObj.firstName = firstname
        eObj.lastName = lastname
        eObj.age = age
        eObj.username = username


        if len(firstname) < 8:
            return render(request, "update.html", {"msg": " firstname has to be min 8 char","Employee":eObj})
        if len(lastname) < 6:
            return render(request, "update.html", {"msg": " lastname has to be min 6 char","Employee":eObj})
        if (age) not in  range(18,60):
            return render(request, "update.html", {"msg": " age has to be in 18-60","Employee":eObj})
        if len(username) < 5:
            return render(request, "update.html", {"msg": " username has to be min 5 char","Employee":eObj})

        eObj.save()

        return render(request, "showEmployee1.html", {"msg": "emp updated"})


"""def handleSort(request):
    (request.method == 'GET')
        list = Employee.object.all()
       
        l1 = Employee.objects.order_by('id') // sort by id
        l2 =Employee.objects.order_by(Lower('firstName').desc()) // desc order  by fname(descending)
        l3 =Employee.objects.order_by(Lower('lastName').asc())  // asc order by lname(assending)

        Employee.objects.all()[:10]
        
        noOfEmps = Employee.objects.count() 
        
        #get details whose name contains kumar(first letter should be capital)
list= Employee.objects.get(firstName__contains="Kumar")

#get details whose name contains kumar ignoring the case 
list= Employee.objects.get(firstName__icontains="Kumar")

#get details whose name starts with raj
list= Employee.objects.get(firstName__startswith="Raj")

#get details whose name starts with raj ignore case
list= Employee.objects.get(firstName__istartswith="Raj")


#get details whose name ends with raj
list= Employee.objects.get(firstName__endswith="Raj")

#get details whose name ends with raj ignore case
list= Employee.objects.get(firstName__iendswith="Raj")

#get the Employees whose id is 800,100,600
list = Employee.objects.filter(id__in=[800,100,600])

#get all Employees whose age greater than 25
lst=Employee.objects.filter(age__gt=25)

#get all Employees whose age less  than  or equal 25
lst=Employee.objects.filter(age__lte=25)

#get all Employees whose age less than 25
lst=Employee.objects.filter(age__lt=25)

#get all Employees whose age greater than  or equal 25
lst=Employee.objects.filter(age__gte=25)

#get all Employees whose account is created today
list = Employee.objects.filter(created_date=datetime.date.today())

#get employees   by range
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2020, 1, 1)
Employees.objects.filter(created_date__range=(start_date, end_date))
	 
#get list of dictionay for all columns
Employee.objects.values()

  
#get list of dictionay for  selected columns
set = Employee.objects.values('id', 'firstName','lastName')
o/p: <QuerySet [{'id': 1, 'firstName': 'kumar' ,'lastName' : 'ram'}]>	(list of dict coloumn)***

#Latest employee created
l= Entry.objects.latest('created_date')	 

#always use (Get all object)***
l1 = list(Entry.objects.all())

update
---------------------
pObj = Employee.objects.get(id=1)
pObj.name="samsung"
pObj.save()
    
#Update(2)
e = Employee.objects.get(id=10)
e.firstName = "ram kumar"
e.save()

  OR
Employee.objects.filter(id=10).update(firstName="ram kumar")

         
         
delete
---------------------------
pObj = Employee.objects.get(id=1)
pObj.delete()  # DELETE SINGLE ROW


         
Employee.objects.all().delete()  ---> delete all
"""



"""
session


when to add the session data
 --------------------------
 when login is success
 
 when to delete the session data
 -----------------------------------
 during the logout
 
 how to add sesison data
 ----------------------------
request.session["id"]=e.id
request.session["fname"] = e.firstName
request.session["lname"] = e.lastName
            
How long is the session data available:
----------------------------------------------
till logout or till session is expired

 
 how to show the session data in the html:
 ----------------------------------------------
  {{request.session.id}}
 {{request.session.fname}}
 {{request.session.lname}}
 
"""

def handleLogin(request):
    if (request.method == 'GET'):
        return render(request, "customerLogin.html", {})

    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]

        eObj = None

        try:
            eObj = Employee.objects.filter(username=username,password=password)
        except:
            return render(request, "customerLogin.html", {"msg": "invalid username or password"})

        if (eObj):
            e=eObj.first()
            request.session["id"]=e.id
            request.session["fname"] = e.firstName
            request.session["lname"] = e.lastName
            return render(request, "customerMenu.html", {"msg": "login sucess"})
        else:
            return render(request, "customerLogin.html", {"msg": "invalid username or password"})

@is_session_active
def handleEmpLogout(request):
    if (request.method == 'GET'):
        # delete the session data during the logout
        del request.session["id"]
        del request.session["fname"]
        del request.session["lname"]
        return render(request, "customerLogin.html", {"msg": "logout sucess"})

"""
pagination:
---------------
->is required when we have large no of records
->customer will not see all the records , hence we show the results in page wise.
->the app has to decide the page size.

ex:
If there is no pagination
in one page show all 27 records


With pagination
we have 27 employees
page 1: show 5 employees  [row 1 to row 5] , offset-0
page 2: show 5 employees  [row 6 to row 10] ,  offset-5
page 3: show 5 employees  [row 11 to row 15] , offset-10
page 4: show 5 employees  [row 16 to row 20] ,  offset-15
page 5: show 5 employees  [row 21 to row 25] ,  offset-20
page 6: show 27 employees [row 26 to row 27]  ,  offset-25

limit -> 5

 steps for pagination:
 ------------------------
 1.Get the list using django orm 
 2.create paginator object using list and paging size
 ex:
   from django.core.paginator import Paginator
   list = Employee.objects.all()
   paginator = Paginator(list, 5)  # 5 is the page size
  
how to get the no of pages:
-------------------------------
pages = paginator.num_pages



how to check if next link/previous link is available?
-------------------------------------------
c1 = paginator.has_previous
c2 = paginator.has_next
  
 
How to get the next/previous page numbers:
---------------------------------------------------

pNo = paginator.previous_page_number
nNo= paginator.next_page_number
 


how to get rows for selected page?
------------------------------------------

paginator = Paginator(Employee.objects.all(), 5)  # 5 is the page size
resultList = paginator.get_page(1)
resultList = paginator.get_page(2)
resultList = paginator.get_page(3)
resultList = paginator.get_page(4)
resultList = paginator.get_page(5)

"""
@is_session_active
def handlePagination(request):
    pageNo = request.GET.get('page')

    #get rows and create Paginator obj
    rows = Employee.objects.all()
    paginator = Paginator(rows, 5)  # 5 is the page size

    #get rows per page
    resultList = paginator.get_page(pageNo)

    allPageNos = [i for i in range(1,paginator.num_pages+1) ]

    return render(request, 'paginationList.html', {'resultList': resultList, 'pageNos':allPageNos })

