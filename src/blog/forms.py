from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = { 
            'title' : forms.TextInput(
                attrs={
                    'id':'subject',
                    'name':'subject',
                    'class':'form-control',
                    'placeholder' : "Article title",
                }
            ),
            'thumbnail' : forms.FileInput(
                attrs={
                    'id':'thumbnail',
                    'name':'thumbnail',
                    'placeholder' : "Thumbnail",
                }
            ),
            'status' : forms.CheckboxInput(
                attrs={
                    'id':'status',
                    'name':'status',
                }
            ),
            'slug' : forms.TextInput(
                attrs={
                    'id':'slug',
                    'name':'slug',
                    'class':'form-control',
                    'placeholder' : "Article slug",
                }
            ),
            'body': SummernoteWidget(
                attrs={
                    'class':'form-control',
                    'placeholder' : "Article body",
                }
            ),
        }
        fields = ['title','thumbnail','status','slug','body']
