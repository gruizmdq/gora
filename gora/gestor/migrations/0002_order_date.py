# Generated by Django 2.2.6 on 2019-10-29 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='MODIFICAR SOLAMENTE EN CASO DE NO SER PARA EL DÍA DE LA FECHA', verbose_name='Fecha del pedido'),
        ),
    ]