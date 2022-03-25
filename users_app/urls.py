from django.urls import path
from .views import UserRegisterView, UserEditSettingsView, UserPasswordChangeView, password_success, \
    ShowProfilePageView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile_settings', UserEditSettingsView.as_view(), name='edit-profile-settings'),
    path('change_password/', UserPasswordChangeView.as_view(), name='password-change'),
    path('password_success', password_success, name='password-success'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create-profile-page'),
    path('profile/id<int:pk>', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('profile/id<int:pk>/edit', EditProfilePageView.as_view(), name='edit-profile-page'),
]
