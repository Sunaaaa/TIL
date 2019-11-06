from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method=="POST":
        # Binding  과정
        # Form 인스턴스를 생성하고, 전달받은 데이터를 채운다.
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
        form = ArticleForm(request.POST)
        
        embed()
        # 유효성 검증
        if form.is_valid():
            # 유효성 검증이 끝난 form은 dict 형태로 뽑혀 나온다.
            # cleaned_data 를 통해 dict 안의 데이터를 검증한다.
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)

        return redirect('articles:detail', article.pk)
    
    else :
        form = ArticleForm()
    # Form으로 전달 받는 형태가 2가지
    # 1. GET 요청 -> 비어있는 Form 전달
    # 2. 유효성 검증 실패 -> 에러 메시지도 담겨서 Form 전달        
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
                                # Class    / PK 값
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else :
        return redirect('articles:detail')


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect('articles:detail', article_pk)

    else :

        form = ArticleForm(initial={
            'title' : article.title,
            'content' : article. content
        })

    # 2가지 Form 형식
    # 1. GET 요청 -> 초기값을 Form에 넣어서 사용자에게 던져줌
    # 2. POST -> is_valid가 False 가 리턴되었을때, 
    #            오류 메시지를 포함해서 사용자에게 던져줌
    context = {
        'form' : form,
    }
    # update와 create 로직에서 동일한 form을 던져주기 때문에 create.html을 랜더링한다.
    return render(request, 'articles/create.html', context)