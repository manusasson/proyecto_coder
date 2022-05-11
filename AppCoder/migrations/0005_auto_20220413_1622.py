# Generated by Django 3.2 on 2022-04-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_auto_20220413_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_contacto', models.EmailField(max_length=254)),
                ('tipo_habitacion', models.CharField(choices=[('Standard Suit', 'Standard Suit'), ('Junior Suit', 'Junior Suit'), ('Deluxe Suit', 'Deluxe Suit'), ('Presidential Suit', 'Presidential Suit')], max_length=50)),
                ('comentario', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento_cliente',
            field=models.CharField(choices=[('CI', 'CI'), ('Pasaporte', 'Pasaporte'), ('DNI', 'DNI')], max_length=250),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='tipo_habitacion_reserva',
            field=models.CharField(choices=[('Standard Suit', 'Standard Suit'), ('Junior Suit', 'Junior Suit'), ('Deluxe Suit', 'Deluxe Suit'), ('Presidential Suit', 'Presidential Suit')], max_length=50),
        ),
    ]