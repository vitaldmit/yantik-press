from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from tinymce.models import HTMLField


class News(models.Model):
    """
    Новости
    """
    TYPE_CHOICES = (
      ('actuals', 'Актуально'),
      ('news', 'Новости'),
      ('publications', 'Публикации'),
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='related_news',
                               verbose_name='Автор',
                               default='')
    type = models.CharField("Тип", max_length=13, choices=TYPE_CHOICES)
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    image = models.ImageField('Главное фото', upload_to='newsimages/%Y/%m/%d/',
                              blank=True, null=True)
    imagesign = models.CharField('Подпись к главному фото', max_length=100,
                                 blank=True, null=True)
    content = HTMLField('Контент', )
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now)
    keywords = models.CharField('Ключевые слова', max_length=100,
                                blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('news:news_article', args=[self.type,
                                                  self.publish.year,
                                                  self.publish.month,
                                                  self.publish.day,
                                                  self.slug])

    class Meta:
        ordering = ('created', )
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class PhotoGallery(models.Model):
    """
    Фотогалерея
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             blank=True, null=True, default=None,
                             verbose_name='Связанная новость',
                             related_name='photogallery')
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    image = models.ImageField('Главное фото', upload_to='newsimages/%Y/%m/%d/',
                              null=True, blank=True)
    visible = models.BooleanField('Показывать', default=1)
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now)

    def get_absolute_url(self):
        return reverse('news:photogallery_article', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug])

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    """
    Изображения для фотогалереи
    """
    photogallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE,
                                     blank=True, null=True, default=None,
                                     verbose_name='Связанная новость',
                                     related_name='news_images')
    image = models.ImageField('Фото', upload_to='newsimages/%Y/%m/%d/',
                              null=True, blank=True)
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created', )
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'

    def __str__(self):
        return self.photogallery.title


class Banners(models.Model):
    TYPE_CHOICES = (
      ('with_image', 'Графический'),
      ('with_text', 'Текстовый'),
      ('with_image_text', 'Текстографический'),
    )
    type = models.CharField("Тип баннера", max_length=15,
                            choices=TYPE_CHOICES, default='image')
    title = models.CharField('Заголовок', max_length=200)
    link = models.CharField('Ссылка', max_length=200)
    image = models.ImageField('Фото баннера',
                              upload_to='bannersimages/%Y-%m-%d/',
                              blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now)
    end_publish = models.DateTimeField("Дата окончания публикации:",
                                       blank=True, null=True)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title
