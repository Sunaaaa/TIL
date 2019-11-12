from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.
# Authentication (인증) -> 신원 확인
# - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

def signup(request):
    
    if request.user.is_authenticated:
        return redirect('articles:index')

    # 사용자를 만드는 로직
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 회원가입 후 바로 로그인 되어 메인페이지로 이동
            auth_login(request.user)

            return redirect('articles:index')


    # 회원가입 Form을 던지는 로직
    else:
        form = CustomUserCreationForm
    
    context = {
        'form' : form,
    }

    return render(request, 'acounts/acount_form.html', context)

def login(request):

    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect('articles:index')
            # next 파라미터에 
            return redirect(request.GET.get('next') or 'articles:index')
    else : 
                                   # For 세션 
        form = AuthenticationForm()

    context = {
        'form' : form,
    } 

    return render(request, 'acounts/acount_form.html', context)

def logout(request):
    # 이 서버를 보고 있는 사용자의 정보가 자동으로 들어가서 로그아웃을 수행한다.
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    # 로그인하고 있는 사람의 session, user 정보가 이미 들어가 있음
    request.user.delete()
    # 지금 접속하고 있는 user 삭제
    return redirect('articles:index')


# 회원정보 수정
@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    else:
        # 회원정보 폼에는 user의 정보가 들어가 있어야 한다.
        # instance로 request.user를 통해 사용자의 정보를 가져온다.
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form' : form
    }

    return render(request, 'acounts/acount_form.html', context)

# 비밀번호 수정
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
        pass

    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form
    }

    return render(request, 'acounts/acount_form.html', context)