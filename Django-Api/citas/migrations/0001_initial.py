# Generated by Django 4.2.2 on 2023-06-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('tipo_identificacion', models.CharField(choices=[(0, 'CEDULA'), (1, 'DOCUMENTO_IDENTIDAD'), (2, 'REGISTRO_CIVIL')], default=0, max_length=100)),
                ('numero_identificacion', models.IntegerField(blank=True, verbose_name='Numero de identificacion')),
                ('telefono', models.IntegerField(verbose_name='Numero de telefono')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Direccion de correo electronico')),
                ('servicio', models.CharField(choices=[(0, 'BARBERIA'), (1, 'MASAJES'), (2, 'PELUQUERIA'), (3, 'UNAS')], default=3, max_length=100)),
                ('profesional', models.CharField(blank=True, max_length=100, verbose_name='Profesional')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha del servicio')),
                ('hora', models.CharField(max_length=100, verbose_name='Hora del servicio')),
            ],
        ),
    ]
