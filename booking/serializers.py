from rest_framework import serializers
from .models import Appointment, Review
from django.core.validators import RegexValidator


class AppointmentSerializer(serializers.ModelSerializer):
    phonenumber = serializers.CharField(validators=[
        RegexValidator(
            r'^\+7\d{10}$',
            'Номер телефона должен быть в формате: "+7xxxxxxxxxx"'
        )
    ])
    name = serializers.CharField(validators=[
        RegexValidator(
            r'^[а-яА-Я\s]*$',
            'Имя может содержать только буквы и пробелы'
        )
    ])

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        return data


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[
        RegexValidator(r'^[a-zA-Zа-яА-Я0-9\s.,!?]*$',
                       'Недопустимые символы.')
    ])
    text = serializers.CharField(validators=[
        RegexValidator(r'^[a-zA-Zа-яА-Я0-9\s.,!?]*$', 'Недопустимые символы.')
    ])
    rating = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['id', 'name', 'text', 'rating']

    def validate(self, data):
        return data
