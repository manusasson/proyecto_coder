# Generated by Django 3.2 on 2022-04-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_auto_20220415_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id_reserva',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]