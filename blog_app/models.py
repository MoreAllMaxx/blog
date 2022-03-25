from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200, )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = "Categories"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=200, null=True, blank=True)
    telegram_url = models.CharField(max_length=200, null=True, blank=True)
    github_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/posts/')
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='post_category', on_delete=models.CASCADE)
    snippet = models.CharField(max_length=200, )
    post_date = models.DateField(auto_now_add=True,)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.name}'

    def total_comments(self):
        return self.objects.count()
