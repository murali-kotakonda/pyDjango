from django.shortcuts import render

# Create your views here.

def htmls_ex1(request):
    return render(request, "Ex1.html", {})

def htmls_ex2(request):
    return render(request, "Ex2.html", {})

def htmls_alert(request):
    return render(request, "alert.html", {})

def htmls_form(request):
    return render(request, "form.html", {})

def htmls_window(request):
    return render(request, "window.html", {})

def htmls_xpath1(request):
    return render(request, "xpath1.html", {})

def htmls_xpath2(request):
    return render(request, "xpath2.html", {})

def htmls_xpath3(request):
    return render(request, "xpath3.html", {})

def htmls_xpath4(request):
    return render(request, "xpath4.html", {})

def htmls_mouse1(request):
    return render(request, "mouse1.html", {})

def htmls_mouse2(request):
    return render(request, "mouse2.html", {})

def htmls_frames(request):
    return render(request, "frames.html", {})

def htmls_table(request):
    return render(request, "table.html", {})

def htmls_links(request):
    return render(request, "links.html", {})

def htmls_drag(request):
    return render(request, "drag.html", {})

def locators(request):
    return render(request, "locators.html", {})

def htmls_index(request):
    return render(request, "htmlIndex.html", {})