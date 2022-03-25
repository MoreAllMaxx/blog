from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import PasswordChangeView

from blog_app.models import Profile
from .forms import SignUpForm, EditProfileSettingsForm, UserPasswordChangeForm, EditUserPageForm


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditSettingsView(UpdateView):
    form_class = EditProfileSettingsForm
    template_name = 'registration/edit_profile_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        stuff_profile = get_object_or_404(Profile, user_id=page_user.id)
        context['url_list'] = [f'<a href="{url}">{name}</a>' for url, name in [
            (stuff_profile.website_url, 'Website'),
            (stuff_profile.telegram_url, 'Telegram'),
            (stuff_profile.github_url, 'Github')
        ] if url is not None
                               ]
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    fields = ['bio', 'profile_pic', 'website_url', 'telegram_url', 'github_url', ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    form_class = EditUserPageForm
    template_name = 'registration/edit_profile_page.html'

    def get_success_url(self):
        return reverse_lazy('show-profile-page', kwargs={'pk': self.request.user.profile.id})
