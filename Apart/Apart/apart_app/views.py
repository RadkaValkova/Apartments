from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from Apart.apart_app.forms import CreateApartmentForm, EditApartmentForm, FilterApartsForm
from Apart.apart_app.models import ApartmentModel

from Apart.core.views import pagination


def home_page(request):
    return render(request, 'home_page.html')


def get_filter_values(values):
    town = values['town'] if 'town' in values else ''
    type = values['type'] if 'type' in values else ''
    construction = values['construction'] if 'construction' in values else ''
    deal = values['deal'] if 'deal' in values else ''

    return {
        'town': town,
        'type': type,
        'construction': construction,
        'deal': deal,
    }


def all_aparts(request):
    aparts_list = ApartmentModel.objects.filter(status__name='активна обява').order_by('id').reverse()

    values = get_filter_values(request.GET)
    town = values['town']
    type = values['type']
    construction = values['construction']
    deal = values['deal']

    if town:
        aparts_list = aparts_list.filter(town__iexact=town)
    if type:
        aparts_list = aparts_list.filter(type=type)
    if construction:
        aparts_list = aparts_list.filter(construction=construction)
    if deal:
        aparts_list = aparts_list.filter(deal=deal)

    # context = {
    #     'aparts': aparts_list,
    #     'form': FilterApartsForm(initial=values),
    # }
    context = {
        'aparts': pagination(request,aparts_list),
        'form': FilterApartsForm(initial=values),
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
            return redirect('profile details')

        context = {
            'form': form,
            'apart': apart,
        }
        return render(request, 'aparts/edit.html', context)


@login_required
def delete_apart(request, pk):
    apart = ApartmentModel.objects.get(pk=pk)
    if request.method == 'POST':
        image = apart.image
        image.delete()
        apart.delete()
        return redirect('profile details')

    context = {
        'apart': apart,
    }
    return render(request, 'aparts/delete.html', context)

