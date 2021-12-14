from analysispage.views import score
from django.shortcuts import render, reverse
from django.http import JsonResponse
from signup.models import User
from .models import UserScore

def index(request):
    context = {'score': score}
    return render(request, 'result_base.html', context)

def saveScore(request):
    if request.GET.get("Data") == "save score":
        login_session = request.session.get('login_session', '')
        userscore_name = User.objects.get(user_id=login_session)

        userscore = UserScore(
            userscore_name = userscore_name,
            userscore_nickname = userscore_name.user_nickname,
            userscore_id = login_session,
            userscore_score = score
        )
        userscore.save()
        return JsonResponse({
            'success': True,
            'url': reverse("mainpage:mainpage")
        })
