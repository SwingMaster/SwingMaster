from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        ranking = []

        for i in range(11):
            a = i+1
            b = 'steve'+chr(65+i)
            c = 90+i
            ranking.append([a,b,c])

        result = {'ranking':ranking}

        return render(request, 'mainpage_base.html', result)

def logout(request):
    request.session.flush()
    return redirect('/')
