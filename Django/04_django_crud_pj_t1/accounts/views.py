from django.shortcuts import render, redirect
from .forms import CustomUserCreateionForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout  as auth_logout

# Create your views here.
def signup(request):
    # 로그인되어 있는 경우, index 페이지로 이동 
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreateionForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            
            return redirect('movies:index')

    else :
        form = CustomUserCreateionForm
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/auth_form.html', context)

def login(request):

    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
            # return redirect('movies:index')
    else :
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request, request.POST)

        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else :
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form' : form,
    }
    return render(request, 'accounts/auth_form.html', context)

def password(request):
    pass
