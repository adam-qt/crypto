from django.http import HttpResponseRedirect
from django.shortcuts import render
from .utils import parse_data_from_api
from .models import Crypto
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.urls import reverse
from django.views.generic import DetailView


class CryptoDetailView(DetailView):
    model = Crypto
    template_name = 'data/detail_view.html'
    context_object_name = 'crypto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        isAdded = False
        context['user'] = ''
        is_log_user = self.request.user.is_authenticated
        if is_log_user:
            if self.object in self.request.user.favourite.all():
                isAdded = True
            user = self.request.user.username
            context['isAdded'] = isAdded
            context['user'] = user
        return context


def data_list_view(request):
    # проверка юзера на аутентификацию
    if request.user.is_authenticated:
        user = request.user.username
    else:
        user = ''
    # обработка сортировки
    if request.GET.get('sort'):
        sort_by = request.GET.get('sort')

    else:
        sort_by = 'price'
    if sort_by != 'name':
        crypto_list = Crypto.objects.all().order_by(f'-{sort_by}')
    else:
        crypto_list = Crypto.objects.all().order_by(f'{sort_by}')

    # обработка поисковой строки
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        crypto_list = Crypto.objects.filter(
            name__istartswith=search_query) | Crypto.objects.filter(
            slug__istartswith=search_query).order_by('name')
        return render(request, 'data/data.html',
                      {'data': crypto_list, 'user': user})

    # пагинация данных
    paginator = Paginator(crypto_list, 8)
    page_number = request.GET.get('page', 1)
    try:
        data = paginator.page(page_number)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'data/data.html', {'data': data, 'user': user})


def favourite_list_view(request):
    data = ''
    if request.user.is_authenticated:
        user_name = request.user.username
        user_object = User.objects.get(username=user_name)
        if user_object.favourite.all().select_related():
            data = user_object.favourite.all().select_related()
    else:

        return HttpResponseRedirect(reverse('data:data'))
    context = {'data': data, 'user': user_name}
    return render(request, 'data/list.html', context=context)


def add_to_favourite_list(request, pk):
    crypto_object = Crypto.objects.get(pk=pk)
    user_object = User.objects.get(username=request.user.username)
    user_object.favourite.add(crypto_object)
    return HttpResponseRedirect(reverse('data:favourite_list'))


def remove_from_favourite_list(request, pk):
    crypto_object = Crypto.objects.get(pk=pk)
    user_object = User.objects.get(username=request.user.username)
    user_object.favourite.remove(crypto_object)
    return HttpResponseRedirect(reverse('data:favourite_list'))


def update(request):
    parse_data_from_api()
    return HttpResponseRedirect(reverse('data:data'))



