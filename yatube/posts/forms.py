from django.forms import ModelForm
from django import forms
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text', 'image')
        labels = {'group': 'Выберите группу', 'text': 'Введите текст'}
        help_text = {'group': 'Любую', 'text': 'Хоть что-то'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
