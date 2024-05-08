from django.db import models


class User(models.Model):
    login = models.CharField(max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=256, verbose_name="Пароль")
    fio = models.CharField(max_length=150, verbose_name="ФИО")


class Cosmetic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    type = models.CharField(max_length=150, verbose_name='Вид продукта')
    country = models.CharField(max_length=150, verbose_name='Страна производитель')
    value_rating = models.IntegerField(verbose_name='Рейтинг')
    count_rating = models.IntegerField(verbose_name='колличество оценок')
    description = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return f'{self.name} [{self.pk}]'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Rating(models.Model):
    cosmetic_id = models.ForeignKey(Cosmetic, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'cosmetic_id'], name='rating')
        ]


