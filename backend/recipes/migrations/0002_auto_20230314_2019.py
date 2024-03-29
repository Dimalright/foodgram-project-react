# Generated by Django 3.2.18 on 2023-03-14 17:19

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientsinrecipe',
            name='amount',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Ингредиента должно быть не менее 1.'), django.core.validators.MaxValueValidator(1000, message='Ингредиента должно быть не более 1000.')], verbose_name='Количество ингредиента'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Время приготовления должно быть не менее 1 минуты!'), django.core.validators.MaxValueValidator(180, message='Время приготовления должно быть не более 180 минут!')], verbose_name='Время приготовления, мин.'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, validators=[django.core.validators.RegexValidator(code='invalid_color_code', message='Значение должно быть в формате HEX (например, #FF0000)', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='Цветовой код'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid_tag_name', message='Разрешены только буквы, цифры и символ подчеркивания', regex='^[a-zA-Z0-9_]+$')], verbose_name='Название тэга'),
        ),
    ]
