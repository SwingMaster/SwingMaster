from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from signup.models import User
from .models import UserScore
from analysispage import views
import random

def index(request):
    login_session = request.session.get('login_session', '')

    if login_session == '':
        return redirect('/')
    else:
        distance = 150
        keyword = ["O.B.", "Bunker", "Hazard", "Hole in One!", "Fairway"]

        if views.score <= 65:
            distance = random.randint(150, 169)
            idx = random.randint(0, 2)
            result = keyword[idx]

        elif views.score > 65 and views.score <= 70:
            distance = random.randint(170, 175)
            result = keyword[4]

        elif views.score > 70 and views.score <= 75:
            distance = random.randint(176, 180)
            result = keyword[4]

        elif views.score > 75 and views.score <= 80:
            distance = random.randint(181, 185)
            result = keyword[4]

        elif views.score > 80 and views.score <= 85:
            distance = random.randint(186, 190)
            result = keyword[4]

        elif views.score > 85 and views.score <= 90:
            distance = random.randint(191, 195)
            result = keyword[4]

        elif views.score > 90 and views.score <= 95:
            distance = random.randint(196, 200)
            result = keyword[4]

        elif views.score > 95 and views.score <= 100:
            distance = random.randint(201, 205)
            result = keyword[4]

            if views.score == 100:
                result = keyword[3]

        context = {'score': views.score, 'distance':distance, 'result':result}
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

