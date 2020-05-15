import os

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
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

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
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

    class Meta:
        ordering = ('created', )
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.post


class Documents(models.Model):
    """ Страница 'Документы' """
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

    class Meta:
        ordering = ('created', )
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


def doc_dir_path(instance, filename):
    slug = instance.documents.slug
    return os.path.join('about/documents/%s/' % slug, filename)


class DocumentsFiles(models.Model):
    """
    Изображения для фотогалереи
    """
    documents = models.ForeignKey(Documents, on_delete=models.CASCADE,
                                  blank=True, null=True, default=None,
                                  verbose_name='Связанные документы',
                                  related_name='documents_files')
    filename = models.CharField('Название документа', max_length=100)
    file = models.FileField('Документ', upload_to=doc_dir_path,
                            max_length=100)
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.documents.title


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
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

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
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

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
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

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
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

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
    map = models.TextField('Карта', blank=True, null=True,
                            help_text="Конструктор: https://yandex.ru/maps/?um=constructor%3A98308fdfb6d76ece12d73780c3ab9e45d1162b227971510aa97ba97a190135cc&source=constructorLink")
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

    class Meta:
        ordering = ('created', )
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title
