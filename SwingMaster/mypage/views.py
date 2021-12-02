from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        return render(request, 'mypage_base.html')