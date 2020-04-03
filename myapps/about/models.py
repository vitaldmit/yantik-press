from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Employees(models.Model):
    """ Страница 'Структура' """
    name = models.CharField('ФИО', max_length=100)
    post = models.CharField('Должность', max_length=100)
    photo = models.ImageField('Фото', upload_to='about/structure/',
                              blank=True, null=True)
    show_photo = models.BooleanField('Показывать фото', default=1)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Почта', max_length=100, blank=True, null=True)
    education = models.TextField('Образование', blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    """ Страница 'Вакансии' """
    post = models.CharField('Должность', max_length=100)
    content = HTMLField('Контент', )
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.post


class Documents(models.Model):
    """ Страница 'Документы' """
    name = models.CharField('Название', max_length=100)
    file = models.FileField('Файл', upload_to='about/documents/%Y-%m-%d/',
                            max_length=100)
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name

class History(models.Model):
    """ Страница 'Документы' """
    title = models.CharField('Заголовок', max_length=100)
    image = models.ImageField('Фото', upload_to='history/%Y/%m/%d/',
                              blank=True, null=True)
    content = HTMLField('Контент', )
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now)

    class Meta:
        ordering = ('created', )
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    """ Страница 'Подписка' """
    title = models.CharField('Заголовок', max_length=100)
    content = HTMLField('Контент', )
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.title


class Advertising(models.Model):
    """ Страница 'Реклама' """
    title = models.CharField('Заголовок', max_length=100)
    content = HTMLField('Контент', )
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'

    def __str__(self):
        return self.title


class Announcing(models.Model):
    """ Страница 'Объявления' """
    title = models.CharField('Заголовок', max_length=200)
    content = HTMLField('Контент', )
    image = models.ImageField('Фото', upload_to='announcing/%Y/%m/%d/',
                              blank=True, null=True)
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Contacts(models.Model):
    """ Страница 'Контакты' """
    title = models.CharField('Заголовок', max_length=100)
    content = HTMLField('Контент', )
    map = models.TextField('Карта', blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title
