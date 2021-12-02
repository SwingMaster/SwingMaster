from django.shortcuts import render, redirect
from signup.models import User

def index(request):
    login_session = request.session.get('login_session', '')
    name = User.objects.get(user_id=login_session)

    if login_session == '':
        return redirect('/')
    else:
        ranking = []

        for i in range(11):
            a = i+1
            b = 'steve'+chr(65+i)
            c = 90+i
            ranking.append([a,b,c])

        result = {'ranking':ranking, 'name': name}

        return render(request, 'mainpage_base.html', result)


def logout(request):
    request.session.flush()
    return redirect('/')
