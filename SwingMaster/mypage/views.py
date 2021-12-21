from django.shortcuts import render, redirect
from signup.models import User
from analysisresultpage.models import UserScore


def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        name = User.objects.get(user_id=login_session)
        nickname = name.user_nickname

        userscore_information = UserScore.objects.filter(userscore_nickname=nickname) & UserScore.objects.order_by(
            '-userscore_register_dttm')

        user_label = []
        userscore_list = []

        for i in range(6):
            try:
                dttm = userscore_information[i].userscore_register_dttm

                user_label.append(str(dttm.hour) + '시'+ ' ' + str(dttm.minute) + '분')
                userscore_list.append(userscore_information[i].userscore_score)
            except:
                break

        mytear = 0
        cnt = 0
        for i in range(len(userscore_information)):
            mytear += userscore_information[i].userscore_score
            cnt += 1

        mytear = int(mytear/cnt)

        result = {'nickname': nickname, 'user_label': user_label, 'userscore_list': userscore_list, 'mytear': mytear}

        return render(request, 'mypage_base.html', result)