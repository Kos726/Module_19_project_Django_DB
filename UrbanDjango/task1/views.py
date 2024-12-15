from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def platform(request):
    title = "Главная страница"

    context = {
        'title': title,
    }

    return render(request, 'first_task/platform.html', context)


class Shop(TemplateView):
    template_name = 'first_task/shop.html'


def products(request):
    title = "Игры"
    text_back = "Вернуться обратно"

    subject = "Выбирите игру"

    list_products = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    len_list = len(list_products)

    games = Game.objects.all()
    len_games = Game.objects.count()


    context = {
        'title': title,
        'button_back': text_back,
        'subject': subject,
        'games': games,
        'len_list': len_games,
    }

    return render(request, 'first_task/games.html', context)


def shopping_cart(request):
    title = "Корзина"
    button_back = "Вернуться обратно"

    list_products = []

    if len(list_products) == 0:
        subject = "Ваша корзина пуста"
    else:
        subject = "Выбранные товары"

    context = {
        'title': title,
        'button_back': button_back,
        'subject': subject,
    }

    return render(request, 'first_task/cart.html', context)


users = ['tor', 'gor', 'frog', 'rog', 'smog']

info_ = {}


# Create your views here.
def sign_up_by_html(request):

    if request.method == "POST":
        # Получение данных
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        # HTTP ответ пользователя

        # Валидация данных
        buyer_find = Buyer.objects.filter(slug=username).count()
        print(buyer_find)
        is_valid_age = int(age) >= 18
        is_valid_user = buyer_find == 0  # если нашел, то >0, значит False
        is_valid_password = password == repeat_password
        print(is_valid_user)
        if is_valid_age is False:
            info_.update({'error': 'Вы должны быть старше 18'})

        elif is_valid_user is False:
            info_.update({'error': 'Пользователь уже существует'})

        elif is_valid_password is False:
            info_.update({'error': 'Пароли не совпадают'})

        # если все проверки пройдены
        elif is_valid_age and is_valid_user and is_valid_password is True:

            Buyer.objects.create(name=username, balance=0, age=age)

            return HttpResponse(f'Приветствуем, {username}!')

        # Если GET
    context = info_

    return render(request, 'first_task/registration_page.html', context)


def sign_up_by_django(request):
    if request.method == "POST":
        # Получение данных
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

        # Валидация данных
        buyer_find = Buyer.objects.filter(slug=username).count()
        is_valid_age = int(age) >= 18
        is_valid_user = buyer_find == 0  # если нашел, то >0, значит False
        is_valid_password = password == repeat_password

        if is_valid_age is False:
            info_.update({'error': 'Вы должны быть старше 18'})

        elif is_valid_user is False:
            info_.update({'error': 'Пользователь уже существует'})

        elif is_valid_password is False:
            info_.update({'error': 'Пароли не совпадают'})

        # если все проверки пройдены
        elif is_valid_age and is_valid_user and is_valid_password is True:

            Buyer.objects.create(name=username, balance=0, age=age)

            return HttpResponse(f'Приветствуем, {username}!')

        # HTTP ответ пользователя
    else:
        form = UserRegister()

        # Если GET
    form_ = {'form': form}
    context = {**form_, **info_}
    return render(request, 'first_task/registration_page.html', context)


def news_page(request):
    title = "Новости"
    button_back = "Вернуться обратно"

    # получаем все посты
    news = News.objects.all()

    # создаем пагинатор
    paginator = Paginator(news, 1)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_news = paginator.get_page(page_number)

    # передаем контекст в шаблон

    page_form = {
        'title': title,
        'button_back': button_back,
    }

    page_news_ = {'page_news': page_news}
    context = {**page_form, **page_news_}
    return render(request, 'first_task/news.html', context)
