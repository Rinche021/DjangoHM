from django.db import models
from django.core.validators import MinValueValidator

def my_Validaror(value):
    if value < 100:
        return models.ValidationError("Цена неподходящая")


class Game(models.Model):
    name = models.CharField(max_length=40)
    for_PC = models.BooleanField(default=True)
    popularity = models.BooleanField(default=False)
    price = models.FloatField(validators=[MinValueValidator(100), my_Validaror])

    def __str__(self):
        return self.name


