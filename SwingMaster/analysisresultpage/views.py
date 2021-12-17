from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from signup.models import User
from .models import UserScore
from analysispage import views

def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        distance = 200
        if views.score == 65:
            distance = 150
        elif views.score == 70:
            distance = 200
        elif views.score == 75:
            distance = 250
        elif views.score == 80:
            distance = 300
        elif views.score == 85:
            distance = 350
        elif views.score == 90:
            distance = 400
        elif views.score == 95:
            distance = 450
        elif views.score == 100:
            distance = 500

        context = {'score': views.score, 'distance':distance}
        return render(request, 'result_base.html', context)

def saveScore(request):
    if request.GET.get("Data") == "save score":
        login_session = request.session.get('login_session', '')
        userscore_name = User.objects.get(user_id=login_session)

        userscore = UserScore(
            userscore_name = userscore_name,
            userscore_nickname = userscore_name.user_nickname,
            userscore_id = login_session,
            userscore_score = views.score
        )
        userscore.save()
        return JsonResponse({
            'success': True,
            'url': reverse("mainpage:mainpage")
        })

