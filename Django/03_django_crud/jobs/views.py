from django.shortcuts import render, redirect
import requests
from faker import Faker
from .models import Job
from decouple import config

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

# GIF URL : api.giphy.com/v1/gifs/search
def job(request):
    name = request.POST.get('name')
    faker = Faker('ko_KR') 

    user = Job.objects.filter(name=name).first()

    if user:
        past_job = user.past_job

    else:
        past_job = faker.job()
        Job.objects.create(name=name,past_job=past_job)
    

# 심화 
    api_url = "http://api.giphy.com/v1/gifs/search"
    api_key = config('KEY')

    data = requests.get(f'{api_url}?api_key={api_key}&q={past_job}&limit=1&lang=ko').json()

    try:
        img_url = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        img_url = None

    context = {
        'name' : name,
        'job': past_job,
        'img_url' : img_url,
    }

    # return redirect('jobs:job')
    return render(request, 'jobs/job.html', context)
