from django.core.exceptions import PermissionDenied

def user_email_valid(function):

    def wrap(request, *args, **kwargs):   
        print(request.user.email)

        if request.user.email.endswith("com") :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

def is_Age_Valid(function):

    def wrap(request, *args, **kwargs):

        age = int(request.session["age"])
        if age>=18 :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

def user_is_employee(function):

    def wrap(request, *args, **kwargs):    

        if request.user.role == 'employee':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap