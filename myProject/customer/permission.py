from django.shortcuts import render


def is_session_active(function):

    def wrap(request, *args, **kwargs):
        try:
            userId = request.session["id"]
            if userId:
                return function(request, *args, **kwargs)
            else:
                return render(request, "customerLogin.html", {"msg": "session closed"})
        except Exception:
            return render(request, "customerLogin.html", {"msg": "session closed"})


    return wrap

