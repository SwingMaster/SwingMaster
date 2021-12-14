from django.shortcuts import render, redirect
from signup.models import User
from analysisresultpage.models import UserScore


def index(request):
    login_session = request.session.get('login_session', '')
    name = User.objects.get(user_id=login_session)
    nickname = name.user_nickname

    userscore_information = UserScore.objects.order_by('-userscore_register_dttm')
    label = ['first', 'second', 'third', 'forth', 'fifth', 'sixth']
    user_label = []
    userscore_list = []

    for i in range(6):
        try:
            user_label.append(label[i])
            userscore_list.append(userscore_information[i].userscore_score)
        except:
            break

    result = {'nickname': nickname, 'user_label':user_label, 'userscore_list':userscore_list}

    if login_session == '':
        return redirect('/')
    else:
        return render(request, 'mypage_base.html', result)