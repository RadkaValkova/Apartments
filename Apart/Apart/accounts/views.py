from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Apart.accounts.forms import LoginForm, RegisterForm, ProfileForm
from Apart.accounts.models import Profile
from Apart.apart_app.models import ApartmentModel
from Apart.core.views import pagination


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home page')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home page')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    user_aparts = ApartmentModel.objects.filter(user_id=request.user.id).order_by('id').reverse()

    context = {
        'form': form,
        'aparts': pagination(request,user_aparts),
        'profile': profile,
    }
    return render(request, 'accounts/profile_details.html', context)


@login_required
def delete_user(request):
    user = request.user
    image = Profile.objects.get(pk=request.user.id).profile_image
    if request.POST:
        image.delete()
        user.delete()
        return redirect('home page')
    return render(request, 'accounts/delete_user.html')


@login_required
def edit_profile(request):
    user_id = request.user.id
    profile = Profile.objects.get(pk=user_id)
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'accounts/edit_profile.html', context)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

        context = {
            'form': form,
            'profile': profile,
        }
        return render(request, 'accounts/edit_profile.html', context)

