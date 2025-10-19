from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'vid/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'vid/video_detail.html', {'video': video})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            v = form.save()
            return redirect('vid:video_detail', pk=v.pk)
    else:
        form = VideoForm()
    return render(request, 'vid/video_form.html', {'form': form})

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('vid:video_detail', pk=video.pk)
    else:
        form = VideoForm(instance=video)
    return render(request, 'vid/video_form.html', {'form': form})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('vid:video_list')
    return render(request, 'vid/video_confirm_delete.html', {'video': video})
