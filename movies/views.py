from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie 
from django.shortcuts import get_list_or_404, get_object_or_404



# Create your views here.
@require_safe
def index(request):
    if request.user.is_authenticated: 
        movies = get_list_or_404(Movie)
        context = {
            'movies': movies,  
        }
        return render(request, 'movies/index.html', context) 
    else:
        redirect('accounts:login')



@require_safe
def detail(request, movie_pk):
    pass


@require_safe
def recommended(request):
    pass