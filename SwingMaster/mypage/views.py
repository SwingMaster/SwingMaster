from django.shortcuts import render, redirect
from signup.models import User
# Create your views here.

def index(request):
    login_session = request.session.get('login_session', '')
    name = User.objects.get(user_id=login_session)
    nickname = name.user_nickname

    result = {'nickname': nickname}

    if login_session == '':
        return redirect('/')
    else:
        return render(request, 'mypage_base.html', result)