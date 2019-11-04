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
# def new(request):
#     return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):

    # POST 요청 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()    
        article_pk = article.pk
        return redirect('articles:detail', article_pk) # 2 URL Namespace

    # GET 요청 -> 사용자에게 폼 보여주기
    else :
        return render(request, 'articles/create.html')




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


# # 게시글 수정
# def edit(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     context = {
#         'article' : article
#     }

#     return render(request, 'articles/edit.html', context)

# 수정된 내용을 전달 받아서 DB에 저장 (반영)
def update(request, article_pk):

    article = Article.objects.get(pk=article_pk)

    # POST 요청 -> DB 수정사항 반영
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article_pk)

    # GET 요청 -> 사용자에게 수정 Form 전달
    else :
        context = {
            'article' : article
        }

        return render(request, 'articles/update.html', context)