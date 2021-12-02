from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from argon2 import PasswordHasher

def index(request):
    if request.method == 'GET':
        return render(request, 'signup_base.html')

    elif request.method == 'POST':
        user_name = request.POST.get('name', '')
        user_id = request.POST.get('id', '')
        user_nickname = request.POST.get('nickname', '')
        user_pw = request.POST.get('pw', '')
        user_pw_confirm = request.POST.get('pw-confirm', '')
        user_email = request.POST.get('email', '')

        try:
            _id = User.objects.get(user_id=user_id)
        except:
            _id = None

        try:
            _nickname = User.objects.get(user_nickname=user_nickname)
        except:
            _nickname = None

        if (user_id or user_pw or user_pw_confirm or user_name or user_nickname or user_email) == '':
            messages.warning(request, '빈칸')
            return redirect('./')
        elif user_pw != user_pw_confirm:
            messages.warning(request, '비밀번호 불일치')
            return redirect('./')
        elif len(user_pw) < 8:
            messages.warning(request, '비밀번호 8자 미만')
            return redirect('./')
        elif '@' not in user_email or '.' not in user_email:
            messages.warning(request, '이메일 형식이 잘못됨')
            return redirect('./')
        elif _id is not None:
            messages.warning(request, '아이디 중복')
            return redirect('./')
        elif _nickname is not None:
            print("닉네임 중복")
            messages.warning(request, '닉네임 중복')
            return redirect('./')
        else:
            user = User(
                user_name = user_name,
                user_id = user_id,
                user_nickname = user_nickname,
                user_pw = PasswordHasher().hash(user_pw),
                user_email = user_email
            )
            user.save()
        return redirect('../startpage')

def checkDuplicatedId(request):
    user_id = request.GET.get('user_id')
    try:
        # 중복 검사 실패
        _id = User.objects.get(user_id=user_id)
    except:
        # 중복 검사 성공
        _id = None
    if _id is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    return JsonResponse(context)

def checkDuplicatedNickname(request):
    user_nickname = request.GET.get('user_nickname')
    try:
        # 중복 검사 실패
        _nickname = User.objects.get(user_nickname=user_nickname)
    except:
        # 중복 검사 성공
        _nickname = None
    if _nickname is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    return JsonResponse(context)