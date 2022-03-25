from django import forms
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post, Category, Profile, Comment
from .forms import PostForm, EditForm, AddCategoryForm, CommentForm


class MainPageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-post_date', '-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked

        stuff_profile = get_object_or_404(Profile, user_id=stuff.author.id)
        context['url_list'] = [f'<a href="{url}">{name}</a>' for url, name in [
            (stuff_profile.website_url, 'Website'),
            (stuff_profile.telegram_url, 'Telegram'),
            (stuff_profile.github_url, 'Github')
        ] if url is not None
                               ]
        comment_form = CommentForm()
        if self.request.user.is_authenticated:
            comment_form.fields['name'].widget = forms.HiddenInput()
            comment_form.fields['name'].widget.attrs['required'] = False
            comment_form.fields['name'].required = False
        context['comments_form'] = comment_form
        return context

    def post(self, request, **kwargs):
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            comment_form.fields['name'].required = False

        if comment_form.is_valid():
            self.object = self.get_object()
            comment_form.cleaned_data['post_id'] = self.object.id
            if request.user.is_authenticated:
                comment_form.cleaned_data['name'] = request.user.username
            else:
                comment_form.cleaned_data['name'] += ' ' + '(anon)'
            Comment.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect(reverse_lazy('article-detail', kwargs={'pk': self.object.id}))
        else:
            context = super().get_context_data(**kwargs)
            context['comments'] = comment_form
            return self.render_to_response(context=context)


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.object.id})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={'pk': self.object.id})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def category_view(request, category):
    category = category.replace('-', ' ')
    category_posts = Post.objects.all().filter(category__name=category)
    return render(request, 'category.html', {'category': category, 'category_posts': category_posts})


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'
    context_object_name = 'post'


class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    ordering = ['name']


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    post.save()
    return HttpResponseRedirect(reverse_lazy('article-detail', args=[str(pk)]))
