from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Apart.apart_app.apart_choices import TYPE_CHOICES
from Apart.apart_app.forms import CreateApartmentForm, EditApartmentForm, FilterApartsForm
from Apart.apart_app.models import ApartmentModel, TypeModel


def home_page(request):
    return render(request, 'home_page.html')


def filter_values(value):
    town = value['town'] if 'town' in value else ''
    type = value['type'] if 'type' in value else ''
    return {
        'town': town,
        'type': type,
    }


def all_aparts(request):
    aparts_list = ApartmentModel.objects.filter(status__name='активна обява')

    values = filter_values(request.GET)
    town = values['town']
    type = values['type']
    if town:
        aparts_list = aparts_list.filter(town__iexact=town)
    if type:
        aparts_list = aparts_list.filter(type__iexact=type)

    context = {
        'aparts': aparts_list,
        'form': FilterApartsForm()
    }

    return render(request, 'aparts/all_aparts.html', context)


def apart_details(request, pk):
    apart = ApartmentModel.objects.get(pk=pk)
    user = apart.user
    is_user = apart.user == request.user
    context = {
        'apart': apart,
        'is_user': is_user,
        'user': user,
    }
    return render(request, 'aparts/details.html', context)


@login_required
def create_apart(request):
    if request.method == 'GET':
        context = {
            'form': CreateApartmentForm()
        }
        return render(request, 'aparts/create.html', context)
    else:
        form = CreateApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            apart = form.save(commit=False)
            apart.user = request.user
            apart.save()
            return redirect('profile details')
        context = {
            'form': form
        }
        return render(request, 'aparts/create.html', context)


@login_required
def edit_apart(request, pk):
    apart = ApartmentModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditApartmentForm(instance=apart)
        context = {
            'form': form,
            'apart': apart,
        }
        return render(request, 'aparts/edit.html', context)
    else:
        form = EditApartmentForm(request.POST, request.FILES, instance=apart)
        if form.is_valid():
            form.save()
            return redirect('all aparts')

        context = {
            'form': form,
            'apart': apart,
        }
        return render(request, 'aparts/edit.html', context)

    # if request.method == 'POST':
    #     form = EditApartmentForm(request.POST, request.FILES, instance=apart)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('all aparts')
    # context = {
    #     'form': EditApartmentForm(instance=apart),
    #     'apart': apart,
    # }
    # return render(request, 'edit.html', context)


@login_required
def delete_apart(request, pk):
    apart = ApartmentModel.objects.get(pk=pk)
    if request.method == 'POST':
        apart.delete()
        return redirect('all aparts')

    context = {
        'apart': apart,
    }
    return render(request, 'aparts/delete.html', context)

# def filter_apart(request):
#     aparts = ApartmentModel.objects.filter(status__name='активна обява')
#
#     values = filter_values(request.GET)
#     town = values['town']
#     if town:
#         aparts = aparts.filter(town__iexact=town)
#
#     context = {
#         'filtered_aparts': aparts,
#         'form': FilterApartsForm()
#     }
#
#     return render(request, 'all_aparts.html', context)''
