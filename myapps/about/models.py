from django.db import models


class Employees(models.Model):
    name = models.CharField('ФИО', max_length=100)
    post = models.CharField('Должность', max_length=100)
    photo = models.ImageField('Фото', upload_to='about/structure/',
                              blank=True, null=True)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Почта', max_length=100)
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
        return self.title


class Vacancies(models.Model):
    post = models.CharField('Должность', max_length=100)
    content = models.TextField('Контент', )
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
