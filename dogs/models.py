from django.db import models


# модель для породы
class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Введите название породы",
    )
    description = models.TextField(
        verbose_name="Описание породы",
        help_text="Введите описание породы",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


# модель для собаки
class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        null=True,
        blank=True,
        related_name="dogs",
        # breed = models.CharField(
        #     max_length=100, verbose_name="Порода", help_text="Введите породу собаки"
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
    )
    date_born = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    """счётчик просмотров"""

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]

    def __str__(self):
        return self.name


class Parent(models.Model):
    dog = models.ForeignKey(
        Dog,
        related_name="parents",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Собака",
    )
    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        null=True,
        blank=True,
        related_name="parent_dogs",
    )
    year_born = models.PositiveIntegerField(
        verbose_name="Год рождения",
        help_text="Укажите год рождения",
        default=0,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Собака родитель"
        verbose_name_plural = "Собаки родители"
        ordering = ["breed", "name"]

    def __str__(self):
        return self.name