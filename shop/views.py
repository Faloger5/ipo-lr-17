# shop/views.py

from django.http import HttpResponse

def home(request):
    """Главная страница с ссылками"""
    return HttpResponse("""
    <h1>Магазин подарочных сертификатов</h1>
    <p>Добро пожаловать в наш магазин!</p>
    <ul>
        <li><a href="/about/">Об авторе</a></li>
        <li><a href="/shop/">О магазине</a></li>
    </ul>
    """)

def about(request):
    """Страница об авторе"""
    return HttpResponse("""
    <h1>Об авторе</h1>
    <p><strong>ФИО:</strong> Доброва Анна</p>
    <p><strong>Группа:</strong> 88ТП</p>
    <p><strong>Вариант:</strong> 9</p>
    <p><strong>Тема:</strong> Создание сайта по продаже сертификатов</p>
    <p><strong>GitHub:</strong> <a href="https://github.com/Faloger5">github.com/Faloger5</a></p>
    <br>
    <p><a href="/">← На главную</a></p>
    """)

def shop(request):
    """Страница о магазине"""
    return HttpResponse("""
    <h1>О магазине</h1>
    <p><strong>Название:</strong> GiftCert — Подарочные сертификаты</p>
    <p><strong>Описание:</strong> Магазин по продаже электронных подарочных сертификатов для любых случаев: дни рождения, свадьбы, корпоративы.</p>
    <p><strong>Ассортимент:</strong></p>
    <ul>
        <li>Сертификаты в рестораны</li>
        <li>Сертификаты в спа-салоны</li>
        <li>Сертификаты в магазины электроники</li>
        <li>Сертификаты на онлайн-курсы</li>
        <li>Универсальные сертификаты номиналом от 500 до 50 000 ₽</li>
    </ul>
    <p><strong>Ссылка по варианту:</strong> <a href="https://surprise.by/" target="_blank">Сайт-аналог</a></p>
    <br>
    <p><a href="/">← На главную</a></p>
    """)