from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.

def index(request):
    loginform = LoginForm()
    context = {'forms':loginform}

    if request.method == 'GET':
        login_session = request.session.get('login_session', '')
        if login_session != '':
            return redirect('/mainpage')
        else:
            return render(request, 'startpage_base.html', context)

    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session.set_expiry(0)
            return redirect('/mainpage')

        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'startpage_base.html', context)