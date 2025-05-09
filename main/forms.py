from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'category', 'banner', 'is_draft']
        

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'add comment...'})
        }

# class EmailShareForm(forms.form):
#     name = forms.CharField()
#     to = forms.EmailField()
#     message = forms.CharField(required=False, widget=forms.Textarea)