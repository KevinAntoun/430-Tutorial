from django.urls import path, include

urlpatterns = [
    path('', include('vid.urls', namespace='vid')),
]
