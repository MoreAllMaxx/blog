from django.shortcuts import get_object_or_404

from .models import Category, Profile


def navbar_context(request):
    context = {
        'cat_menu': Category.objects.all(),
    }
    user_profile = Profile.objects.all().filter(user_id=request.user.id)
    if request.user.is_authenticated and user_profile:
        context.update({'user_profile': user_profile[0]})
    return context
