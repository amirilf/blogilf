from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Article


class NewArticleForm(forms.ModelForm):
    def __init__(self, user,edit, *args, **kwargs):
        self.user = user
        self.edit = edit
        
        super().__init__(*args, **kwargs)

    def clean(self):
        
        cleaned_data = self.cleaned_data

        # This validation means that the user cant have the same slug for multiple articles
        # But users can have articles with the same slug
        if not self.edit:
            if Article.objects.filter(slug=cleaned_data['slug'],author=self.user.pk).exists():
                raise forms.ValidationError({'slug': ["Article with this slug already exists.",]})            
            return cleaned_data


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
            'tags': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder' : "Enter tags...",
                    'name':'tags',
                }
            ),
        }
        fields = ['title','thumbnail','status','slug','body','tags']