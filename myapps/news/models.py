from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator
from .tokens import TELEGRAM_TOKEN, VK_TOKEN

from tinymce.models import HTMLField
from html import unescape
import requests


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
                               related_name='news_author',
                               verbose_name='Автор',
                               default='')
    type = models.CharField("Тип", max_length=13, choices=TYPE_CHOICES)
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    image = models.ImageField('Главное фото', upload_to='newsimages/%Y/%m/%d/',
                              blank=True, null=True)
    imagesign = models.CharField('Подпись к главному фото', max_length=70,
                                 blank=True, null=True,
                                 help_text='Короткое описание к главному фото')
    content = HTMLField('Контент', )
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    visible = models.BooleanField('Показывать', default=1)
    # ontop = models.BooleanField('Размещать сверху', )
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")
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

    def save(self, *args, **kwargs):
        absolute_url = 'https://yantik-press.ru' + self.get_absolute_url()
        message = unescape(strip_tags(self.content))
        truncated_message = Truncator(message).words(30)

        # Разместить на каналах в Telegram
        token = TELEGRAM_TOKEN
        chat_ids = ['@yantik_press', '@yantik_news']
        for chat_id in chat_ids:
            requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token),
                         params=dict(chat_id=chat_id, text=absolute_url))

        # Разместить на странице в контакте
        token = VK_TOKEN
        group_id = -184997347
        requests.post('https://api.vk.com/method/wall.post',
                      data={'access_token': token,
                            'owner_id': group_id,
                            'from_group': 1,
                            'message': truncated_message,
                            'attachments': absolute_url,
                            'signed': 0,
                            'v': "5.110"}).json()

        super(News, self).save(*args, **kwargs)


class PhotoGallery(models.Model):
    """
    Фотогалерея
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             blank=True, null=True, default=None,
                             verbose_name='Связанная новость',
                             related_name='photogallery_news')
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    image = models.ImageField('Главное фото', upload_to='newsimages/%Y/%m/%d/',
                              null=True, blank=True)
    content = HTMLField('Контент', null=True, blank=True)
    visible = models.BooleanField('Показывать', default=1)
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

    def get_absolute_url(self):
        return reverse('news:photogallery_article', args=[self.publish.year,
                                                          self.publish.month,
                                                          self.publish.day,
                                                          self.slug])

    def get_subfeature_photos(self):
        return self.photogallery_images.filter(visible=True)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалереи'

    def __str__(self):
        return self.title


class PhotoGalleryImages(models.Model):
    """
    Изображения для фотогалереи
    """
    photogallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE,
                                     blank=True, null=True, default=None,
                                     verbose_name='Связанная новость',
                                     related_name='photogallery_images')
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


class VideoNews(models.Model):
    """
    Видеоновости
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             blank=True, null=True, default=None,
                             verbose_name='Связанная новость',
                             related_name='videonews')
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('ЧПУ', max_length=200, unique_for_date='publish')
    image = models.ImageField('Фото', upload_to='newsvideos/%Y/%m/%d/',
                              null=True, blank=True,
                              help_text="Превью изображение видео")
    video = models.FileField('Видео', upload_to='newsvideos/%Y/%m/%d/',
                             null=True, blank=True)
    cap = models.CharField('Видео CAP.RU', max_length=150,
                           null=True, blank=True)
    youtube = models.CharField('Видео YouTube', max_length=100,
                               null=True, blank=True, help_text='Код видео')
    instagram = models.CharField('Видео Instagram', max_length=100,
                                 null=True, blank=True)
    kod = models.TextField('Код для вставки', blank=True, null=True)
    content = HTMLField('Контент', null=True, blank=True)
    visible = models.BooleanField('Показывать', default=1)
    source = models.CharField('Первоисточник', max_length=150,
                              blank=True, null=True)
    created = models.DateTimeField('Создан', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField('Обновлен',
                                   auto_now=True, auto_now_add=False)
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")

    def get_absolute_url(self):
        return reverse('news:videonews_article', args=[self.publish.year,
                                                       self.publish.month,
                                                       self.publish.day,
                                                       self.slug])

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Видеоновости'
        verbose_name_plural = 'Видеоновости'

    def __str__(self):
        return self.title


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
    publish = models.DateTimeField("Дата публикации", default=timezone.now,
                                   help_text="Дата и время публикации")
    # end_publish = models.DateTimeField("Дата окончания публикации:",
    #                                    blank=True, null=True)

    class Meta:
        ordering = ('created', )
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.title
