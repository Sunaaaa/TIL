from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'god' : "오현무 사성규"
    }
    return render(request, 'index.html', context)


# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
# request를 통해서 정보가 들어온다.
def catch(request):
    # GET으로 보내면 request를 통해서 GET 정보가 들어온다. JSON/딕셔너리
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    
    return render(request, 'catch.html', context)


# [실습] 아스키 아트 API를 통한 요청-응답 실습
# 사용자로부터 텍스트를 입력받는 페이지
def art(request):    
    return render(request, 'art.html')

# 텍스트 받아서 아스키 아트로 보여주는 페이지
def result(request):
    message = request.GET.get('text')
    art = "http://artii.herokuapp.com/make?text=" + message
    context = {
        'art' : art
    }
    
    return render(request, 'result.html', context)
