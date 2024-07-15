from django import forms
from .models import Post, Comment,Category
from django.contrib.auth.models import User

choices = Category.objects.all().values_list('name','name')
choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'title_tag','text','category','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass',}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
                 }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
