# Generated by Django 3.2 on 2022-04-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_reserva_tipo_habitacion_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento_cliente',
            field=models.CharField(choices=[('TICKET', 'Ticket created'), ('TICKET_HISTORY', 'Ticket changed'), ('TICKET_RATE', 'Ticket rated'), ('PASSWORD_CHANGE', 'Password changed'), ('CONTENT', 'Added content')], max_length=250),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='tipo_habitacion_reserva',
            field=models.CharField(choices=[('TICKET', 'Ticket created'), ('TICKET_HISTORY', 'Ticket changed'), ('TICKET_RATE', 'Ticket rated'), ('PASSWORD_CHANGE', 'Password changed'), ('CONTENT', 'Added content')], max_length=50),
        ),
    ]