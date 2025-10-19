from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'actor1', 'actor2', 'director', 'genre', 'release_year']
        labels = {
            'title': 'MovieTitle',
            'actor1': 'Actor1Name',
            'actor2': 'Actor2Name',
            'director': 'DirectorName',
            'genre': 'MovieGenre',
            'release_year': 'ReleaseYear',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'actor1': forms.TextInput(attrs={'class': 'form-control'}),
            'actor2': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }
