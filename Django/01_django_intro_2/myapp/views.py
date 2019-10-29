from django.shortcuts import render
import requests, random

# Create your views here.
def index(request):
    context = {
        'god' : "오현무 사성규"
    }
    return render(request, 'myapp/index.html', context)


# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'myapp/throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
# request를 통해서 정보가 들어온다.
def catch(request):
    # GET으로 보내면 request를 통해서 GET 정보가 들어온다. JSON/딕셔너리
    print(request)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message' : message
    }
    
    return render(request, 'myapp/catch.html', context)


# [실습] 아스키 아트 API를 통한 요청-응답 실습
# 사용자로부터 텍스트를 입력받는 페이지
def art(request):    
    return render(request, 'myapp/art.html')

# 텍스트 받아서 아스키 아트로 보여주는 페이지
# def result(request):
#     message = request.GET.get('text')
#     art = "http://artii.herokuapp.com/make?text=" + message
#     context = {
#         'art' : art
#     }
    
#     return render(request, 'myapp/result.html', context)

def result(request):
    # 1. form 태그로 날린 데이터를 받는다. (GET 방식)
    word = request.GET.get('text')
    # 2. ARTII api로 요청을 보내 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')
    # 4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장한다.
    font = random.choice(fonts)
    # 5. 위에서 우리가 만든 word와 font를 가지고 다시 요청을 보내 응답 결과를 result에 저장
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {'art': result}

    return render(request, 'myapp/result.html', context)


# 회원가입 폼을 보여주는 페이지
def user_new(request):
    return render(request, 'myapp/user_new.html')

# 회원가입 요청을 처리하는 페이지 (로직)
def user_create(request):
    user_id = request.POST.get('user_id')
    pw = request.POST.get('pw')

    context = {
        'user_id' : user_id,
        'pw' : pw,
    }
    return render(request, 'myapp/user_create.html', context)

# 회원가입 폼을 보여주는 페이지
def static_sample(request):
    return render(request, 'myapp/static_sample.html')