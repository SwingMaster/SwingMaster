from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    ranking = []

    for i in range(11):
        a = i+1
        b = 'steve'+chr(65+i)
        c = 90+i
        ranking.append([a,b,c])

    result = {'ranking':ranking}

    return render(request, 'mainpage_base.html', result)
