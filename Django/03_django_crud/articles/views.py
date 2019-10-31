from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles
    }

    # 거꾸로
    # articles = Article.objects.all()[::-1]
    return render(request, 'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):

    # POST 방식으로 사용자가 입력한 데이터를 받는다.
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 인스턴스를 생성하여 데이터 베이스에 저장한다. 
    article = Article(title=title, content=content)
    article.save()
   
    article_pk = article.pk

    # return redirect(f'/articles/{article_pk}') # 1
    return redirect('articles:detail', article_pk) # 2 URL Namespace

    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용했을 때 (헷갈림 주의!)
    # <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a> 



# 게시글 상세 정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


# 게시글 삭제
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


# 게시글 수정
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }

    return render(request, 'articles/edit.html', context)

# 수정된 내용을 전달 받아서 DB에 저장 (반영)
def update(request, article_pk):

    # 1. 수정할 게시글 인스턴스 가져오기
    article = Article.objects.get(pk=article_pk)

    # 2. 폼에서 전달받은 데이터 덮어쓰기
    title = request.POST.get('title')
    content = request.POST.get('content')
    article.title = title
    article.content = content
    
    # 3. DB 저장
    article.save()

    # 3. DB 저장 완료 후 게시글 detail로 이동
    # return redirect(f'/articles/{article_pk}')
    return redirect('articles:detail', article_pk)