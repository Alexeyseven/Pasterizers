from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату регистрации."""
    reg_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class Persons(CreatedModel):
    name = models.TextField(
        verbose_name='Имя',
        help_text='Имя сотрудника')
    sirname = models.TextField(
        verbose_name='Фамилия',
        help_text='Фамилия сотрудника')
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.sirname

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employes'


class Media(models.Model):
    title = models.TextField(
        verbose_name='Название',
        help_text='Название произведения'
    )
    actors = models.ManyToManyField(Persons)

    def __str__(self) -> str:
        return self.title