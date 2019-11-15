from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def new(request):
    if request.method == 'POST':

        title =request.POST.get('title')
        description = request.POST.get('description')
        user = request.user

        image = request.FILES.get('image')
        movie = Movie(title=title, description=description, poster=image)

        movie.user = user
        movie.save()

        return redirect('movies:index')

    else:
        return render(request, 'movies/form.html')


def detail(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie' : movie,
    }

    return render(request, 'movies/detail.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')

def edit(request):
    if request.method == "POST":

    
    else : 
        form = 
    context = {
        'form' : form,
    }

    return render(request, 'movies/form.html', context)
        
