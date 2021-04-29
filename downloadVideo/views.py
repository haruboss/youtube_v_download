from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import TemplateView
import youtube_dl
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def download_video(request):
    if request.method == 'POST':
        video_url = request.POST['url']
        if video_url:
            ydl_opts = {'outtmp1': 'D:/'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messages.success(request, 'Video Downloaded.')
            return redirect('downloadVideo:home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('downloadVideo:home')
    return redirect('downloadVideo:home')
