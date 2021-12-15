from django.shortcuts import render, redirect


def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        return render(request, 'editprofile_base.html')
