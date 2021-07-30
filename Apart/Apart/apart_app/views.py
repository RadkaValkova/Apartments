from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

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


# class ApartList(ListView):
#     model = ApartmentModel
#     template_name = 'aparts/all_aparts.html'
#     # context_object_name = 'aparts'
#     # form_class = FilterApartsForm
#     paginate_by = 10
#
#     # def get_queryset(self):
#     #     aparts = super().get_queryset()
#     #
#     #     town = self.request.GET.get('town', '')
#     #     type = self.request.GET.get('type', '')
#     #     construction = self.request.GET.get('construction', '')
#     #     deal = self.request.GET.get('deal', '')
#     #     if town:
#     #         return aparts.filter(town__icontains=town)
#     #     if type:
#     #         return aparts.filter(type=type)
#     #     if construction:
#     #         return aparts.filter(construction=construction)
#     #     if deal:
#     #         return aparts.filter(deal=deal)
#     #
#     #     # self.filterset = self.filterset_class(self.request.GET, queryset=aparts)
#     #     # return self.filterset.qs.distinct()
#
#     def get_queryset(self):
#         # aparts = super(ApartList, self).get_queryset()
#         aparts = super().get_queryset()
#         # aparts = self.model.objects.all()
#         town = self.request.GET.get('town', '')
#         type = self.request.GET.get('type', '')
#         construction = self.request.GET.get('construction', '')
#         deal = self.request.GET.get('deal', '')
#         if town:
#             return aparts.filter(town__icontains=town)
#         if type:
#             return aparts.filter(type=type)
#         if construction:
#             return aparts.filter(construction=construction)
#         if deal:
#             return aparts.filter(deal=deal)
#         return aparts
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     # Pass the filterset to the template - it provides the form.
#     #     context['aparts'] = self.get_queryset()
#     #     context['form'] = FilterApartsForm()
#     #     return context
#
#     def get_context_data(self, **kwargs):
#         # context = super(ApartList, self).get_context_data(**kwargs)
#         context = super().get_context_data(**kwargs)
#         context['aparts'] = self.get_queryset()
#         context['form'] = FilterApartsForm()
#         return context


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


# @login_required
# def delete_apart(request, pk):
#     apart = ApartmentModel.objects.get(pk=pk)
#     if request.method == 'POST':
#         apart.delete()
#         return redirect('profile details')
#
#     context = {
#         'apart': apart,
#     }
#     return render(request, 'aparts/delete.html', context)

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

# class ApartDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'aparts/delete.html'
#     model = ApartmentModel
#     success_url = reverse_lazy('profile details')
