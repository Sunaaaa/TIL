from django.shortcuts import render, redirect
from .models import Movie
from .models import Comment


# Create your views here.
def index(request):

    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }

    return render(request, 'movies/index.html', context)

# def new(request):
#     return render(request, 'movies/new.html')


def create(request):

    if request.method == 'POST':
        movie = Movie()
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')

        movie.save()

        return redirect('movies:detail', movie.pk)
    
    else :
        return render(request, 'movies/create.html')
    

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comments' : comments,
    }

    return render(request, 'movies/detail.html', context)


# def edit(request, movie_pk):
#     movie = Movie.objects.get(pk=movie_pk)
#     context = {
#         'movie' : movie
#     }

#     return render(request, 'movies/edit.html', context)


def update(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    
    if request.method == 'POST':

        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')

        movie.save()

        context = {
            'movie' : movie,
        }
        return redirect('movies:detail', movie.pk)

    else :
        movie = Movie.objects.get(pk=movie_pk)
        context = {
            'movie' : movie,
            'comments' : comments,
        }

        return render(request, 'movies/update.html', context)


def delete(request, movie_pk):

    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_pk)
        movie.delete()

    return redirect('movies:index')


def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.movie = movie
    
        comment.save()
        
    return redirect('movies:detail', movie_pk)

def comments_delete(request, movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)    
        comment.delete()

    return redirect('movies:detail', movie_pk)

