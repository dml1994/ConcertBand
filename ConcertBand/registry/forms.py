from django import forms
from .models import *

class ComposerForm(forms.ModelForm):
 
    class Meta:
        model = Composer
 
        fields = [
            "name",
            "surname",
            "web",
            "biography",
            "photo"
        ]

class ScoreForm(forms.ModelForm):
 
    class Meta:
        model = Score
 
        fields = [
            "title",
            "composers",
            "genre",
            "registry",
            "arrangers",
            "mp3",
            "video"
        ]

class ScoreGenreForm(forms.ModelForm):
 
    class Meta:
        model = ScoreGenre
 
        fields = [
            "name"
        ]
class SheetForm(forms.ModelForm):
 
    class Meta:
        model = Sheet
 
        fields = [
            "pdf",
            "category",
            "score"
        ]

class SheetCategoryForm(forms.ModelForm):
 
    class Meta:
        model = SheetCategory
 
        fields = [
            "name"
        ]

class VideoMediaForm(forms.ModelForm):
 
    class Meta:
        model = VideoMedia
 
        fields = [
            "title",
            "url"
        ]