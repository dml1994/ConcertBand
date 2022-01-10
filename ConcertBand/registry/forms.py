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

class ScoreGenreForm(forms.ModelForm):
 
    class Meta:
        model = ScoreGenre
 
        fields = [
            "name"
        ]

class SheetCategoryForm(forms.ModelForm):
 
    class Meta:
        model = SheetCategory
 
        fields = [
            "name"
        ]