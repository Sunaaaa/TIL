from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.

# view 함수는 중간 관리자
# 사용자가 접속해서 볼 페이지를 작성한다.
# 즉, 하나하나의 페이지를 'view'라고 부른다.
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.
# 필수적으로 첫번째 인자는 반드시 request!
def index(request):
    # 첫번째 return 도 반드시 request
    return render(request, 'index.html')

# def introduce(request):
#     name = '폴킴'

#     # render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다. 
#     return render(request, 'introduce.html', {'name' : name})


# 메뉴 하나를 랜덤으로 골라 return 
def dinner(request):
    menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
    today_pick = random.choice(menu)

    # 넘겨야 할 데이터가 2개 이상이면 context라는 변수 명에 담아서 넘겨준다.
    context = {
        'pick' : today_pick
    }

    return render(request, 'dinner.html', context)


# Lorem Picsum 사용해서 랜덤 이미지를 보여주는 페이지 만들기!
def image(request):
    img = "https://picsum.photos/200/300"
    context = {
        'img' : img
    }

    return render(request, 'image.html', context)

def hello(request, name):
    menu = ['초밥', '삼겹살', '치즈돈까스', '살치살 스테이크']
    today_pick = random.choice(menu)

    context = {
        'name' : name,
        'pick' : today_pick,
        }
    return render(request, 'hello.html', context)


# 실습 1
# 템플릿 변수를 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자
def introduce(request, name, age, hobby, speciality):
    context = {
        'name' : name,
        'age' : age,
        'hobby' : hobby,
        'speciality' : speciality,
        }
    return render(request, 'introduce.html', context)


# 실습 2
# 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자!
def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
        }
    return render(request, 'times.html', context)

# 실습 3
# 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자
def radius(request, rad):
    result = 3.14 * rad*rad
    context = {
        'rad' : rad,
        'result' : result,
        }
    return render(request, 'radius.html', context)


# 추가 실습
# 동적 라우팅으로 이미지 너비, 높이를 받아서 이미지 출력하는 페이지
def imageSize(request, width, height):
    img = "https://picsum.photos/"+width + "/"+height
    context = {
        'img' : img,  
    }

    return render(request, 'imageSize.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)



