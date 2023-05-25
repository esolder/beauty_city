from datetime import date
from dateutil.relativedelta import relativedelta
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='services',
        verbose_name='Категория',
    )
    price = models.DecimalField(
        'Цена',
        default=0,
        decimal_places=2,
        max_digits=10,
    )
    image = models.ImageField(
        'Изображение',
        blank=True,
    )


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField('Специальность', max_length=50)

    class Meta:
        verbose_name = 'Специальность сотрудника'
        verbose_name_plural = 'Специальности сотрудников'

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.PROTECT,
        related_name='employees',
        verbose_name='Специальность',
    )
    start_work_date = models.DateField('Дата начала работы')
    photo = models.ImageField('Фото', blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def experience(self):
        today = date.today()
        experience_delta = relativedelta(today, self.start_work_date)
        years = experience_delta.years
        months = experience_delta.months
        return f'{years} г. {months} мес.'
    

@receiver(pre_delete, sender=Employee)
def delete_photo(sender, instance, **kwargs):
    instance.photo.delete()


class Appointment(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name='appointments',
        verbose_name='Услуга',
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='appointments',
        verbose_name='Сотрудник',
    )
    date = models.DateField('Дата записи')
    time = models.TimeField('Время записи')
    name = models.CharField('Имя клиента', max_length=100)
    phonenumber = PhoneNumberField('Телефон клиента', max_length=20)
    comment = models.TextField('Комментарий клиента', blank=True)

    class Meta:
        ordering = ['-date', '-time']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
