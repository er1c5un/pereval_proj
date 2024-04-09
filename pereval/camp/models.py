from django.db import models
from django.utils.translation import gettext_lazy as _


class PerevalManager(models.Manager):
    def submit_data(self, name, description):
        pereval_instance = self.create(name=name, description=description)
        return pereval_instance


class Tourists(models.Model):
    """
    Модель пользователей (туристов)
    """
    fam = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    otc = models.CharField(max_length=100, verbose_name="Отчество")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон")


class Pereval(models.Model):
    """
    Модель перевала. Хранит в себе основные данные
    """
    class Status(models.TextChoices):
        NEW = "NW", _("Новый")
        PENDING = "PN", _("В работе")
        ACCEPTED = "AC", _("Принято")
        REJECTED = "RJ", _("Не принято")

    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100)
    connect = models.CharField(max_length=100, default="", verbose_name='Что соединяет')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.labels[0], verbose_name='Состояние')
    tourist_id = models.ForeignKey(to=Tourists, related_name='pereval_user', on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    coord_id = models.OneToOneField(to='Coords', related_name='pereval_coord', on_delete=models.CASCADE,
                                    verbose_name='Координаты')
    level_id = models.ForeignKey(to='Level', related_name='pereval_level', on_delete=models.CASCADE,
                                 verbose_name='Сложность', null=True)


class Coords(models.Model):
    """
    Модель для координат
    """
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")


class Level(models.Model):
    """
    Модель для уровней сложности перевала
    """
    class Levels(models.TextChoices):
        LEVEL1 = "LV1", _("1А")
        LEVEL2 = "LV2", _("1Б")
        LEVEL3 = "LV3", _("2А")
        LEVEL4 = "LV4", _("2Б")
        LEVEL5 = "LV5", _("3А")
        LEVEL6 = "LV6", _("3Б")

    winter = models.CharField(max_length=3, choices=Levels.choices, default=Levels.LEVEL1, verbose_name="Зима")
    spring = models.CharField(max_length=3, choices=Levels.choices, default=Levels.LEVEL1, verbose_name="Весна")
    summer = models.CharField(max_length=3, choices=Levels.choices, default=Levels.LEVEL1, verbose_name="Лето")
    autumn = models.CharField(max_length=3, choices=Levels.choices, default=Levels.LEVEL1, verbose_name="Осень")


class Images(models.Model):
    """
    Модель для фотографий
    """
    images = models.ImageField(upload_to='static/images', verbose_name="Фото", default='default_image.jpg')
    title = models.CharField(max_length=100, verbose_name="Название")
    pereval_id = models.ForeignKey(to=Pereval, related_name='images', on_delete=models.CASCADE,
                                   verbose_name='Фотографии', null=True)
