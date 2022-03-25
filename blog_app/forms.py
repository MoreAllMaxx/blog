from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'category', 'snippet', 'body',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Post Category'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Snippet'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Body'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Post Category'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Body'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Title'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'text': forms.Textarea(attrs={'cols': '50', 'rows': '3', 'class': 'form-control',
                                          'placeholder': 'Comment Text', 'aria-label': 'hidden'},),
        }
        labels = {
            'name': '',
            'text': '',
        }
