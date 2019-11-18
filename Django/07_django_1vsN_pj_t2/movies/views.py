from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm, RatingForm
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
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            user = request.user
            movie.user = user
            movie.save()
            return redirect('movies:detail', movie.pk)

    else:
        form = MovieForm
    
    context = {
        'form' : form ,
    }

    return render(request, 'movies/new.html', context)

# @login_required
# def new(request):
#     if request.method == 'POST':

#         title =request.POST.get('title')
#         description = request.POST.get('description')
#         user = request.user

#         image = request.FILES.get('image')
#         movie = Movie(title=title, description=description, poster=image)

#         movie.user = user
#         movie.save()

#         return redirect('movies:index')

#     else:
#         return render(request, 'movies/form.html')



def detail(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    ratings = movie.rating_set.all()
    form = RatingForm()

    context = {
        'movie' : movie,
        'ratings' : ratings,
        'form' : form,
    }

    return render(request, 'movies/detail.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')

def edit(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie_pk)

    else : 
        form = MovieForm(instance=movie)
    context = {
        'form' : form,
    }

    return render(request, 'movies/new.html', context)
    


def rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        
        rating_form = RatingForm(request.POST)

        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            user = request.user
            rating.user = user
            rating.movie = movie
            rating.save()

    return redirect('movies:detail', movie_pk)
