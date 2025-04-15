from django.shortcuts import render

def Mainpage(request):
    return render(request, 'Mainpage.html')


def Navbar(request):
    return render(request, 'Navbar.html')
def Mainpagetwo(request):
    return render(request, 'Mainpagetwo.html')
def Mainthree(request):
    return render(request, 'Mainthree.html')    