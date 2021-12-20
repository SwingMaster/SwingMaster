from django.shortcuts import render, redirect
from signup.models import User
from analysisresultpage.models import UserScore
from collections import defaultdict

def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        name = User.objects.get(user_id=login_session)

        userscore_information = UserScore.objects.all()
        dict = defaultdict(list)
        userscore_dict = defaultdict()
        for i in userscore_information:
            dict[i.userscore_name].append(i.userscore_score)

        for i, v in dict.items():
            userscore_dict[i] = sum(v)/len(v)

        userscore_list = []
        for i, v in userscore_dict.items():
            userscore_list.append([i, v])
        userscore_list.sort(key=lambda x:-x[1])

        ranking = []

        for i in range(11):
            try:
                No = i + 1
                Name = userscore_list[i][0]
                Value = int(userscore_list[i][1])
                ranking.append([No, Name, Value])
            except:
                break

        result = {'ranking':ranking, 'name': name}

        return render(request, 'mainpage_base.html', result)


def logout(request):
    request.session.flush()
    return redirect('/')
