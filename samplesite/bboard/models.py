from django.db import models
from django.core.validators import MinValueValidator, ValidationError


def my_validator(value):
    if value < 0:
        return models.ValidationError("Произошла ошибка !")


class Person(models.Model):
    name = models.CharField(max_length=15)
    work = models.BooleanField(default=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0, message="Вы не существуете"), my_validator])

    def get_id_name(self):
        return f"id: {self.id}, " \
               f"Имя: {self.name}"

    def get_age(self):
        return self.age

    @classmethod
    def get_total_age(cls):
        return cls.objects.aggregate(total_age=models.Sum('age'))['total_age']


class Child(models.Model):
    parents = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    study = models.BooleanField(default=True)

    def get_id_name(self):
        return f"id: {self.id}, " \
               f"Имя: {self.name}"

    def get_age(self):
        return self.age

    @classmethod
    def get_total_age(cls):
        return cls.objects.aggregate(total_age=models.Sum('age'))['total_age']


class Icecream(models.Model):
    size = models.CharField(max_length=50)
    type_ = models.CharField(max_length=40)
    price = models.FloatField()

    def get_id_size(self):
        return f"id: {self.id}, " \
               f"Размер: {self.size}"

    def get_price(self):
        return self.price

    @classmethod
    def get_total_price(cls):
        return cls.objects.aggregate(total_price=models.Sum('price'))['total_price']


class IcecreamMarket(models.Model):
    ice_creams = models.ManyToManyField(Icecream)
    size_building = models.CharField(max_length=10)
    description = models.CharField(max_length=2000)

    def get_id_description(self):
        return f"id: {self.id}, " \
               f"Описание: {self.description}"

    @property
    def total_ice_creams(self):
        return self.ice_creams.count()
