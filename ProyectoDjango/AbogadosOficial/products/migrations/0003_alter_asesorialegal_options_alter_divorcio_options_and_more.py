# Generated by Django 5.1.3 on 2024-11-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_serviciolegal_fecha_solicitud_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asesorialegal',
            options={'verbose_name': 'Asesoría Legal', 'verbose_name_plural': 'Asesorías Legales'},
        ),
        migrations.AlterModelOptions(
            name='divorcio',
            options={'verbose_name': 'Servicio de Divorcio', 'verbose_name_plural': 'Servicios de Divorcio'},
        ),
        migrations.AlterModelOptions(
            name='serviciolegal',
            options={'verbose_name': 'Servicio Legal', 'verbose_name_plural': 'Servicios Legales'},
        ),
        migrations.RenameField(
            model_name='asesorialegal',
            old_name='especialidad',
            new_name='_especialidad',
        ),
        migrations.RenameField(
            model_name='asesorialegal',
            old_name='num_asesorias',
            new_name='_num_asesorias',
        ),
        migrations.RenameField(
            model_name='divorcio',
            old_name='duracion_estimada',
            new_name='_duracion_estimada',
        ),
        migrations.RenameField(
            model_name='divorcio',
            old_name='num_divorcios',
            new_name='_num_divorcios',
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='costo',
            new_name='_costo',
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='descripcion',
            new_name='_descripcion',
        ),
        migrations.AlterField(
            model_name='serviciolegal',
            name='fecha_solicitud',
            field=models.DateField(blank=True, db_column='fecha_solicitud', null=True),
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='fecha_solicitud',
            new_name='_fecha_solicitud',
        ),
        migrations.RenameField(
            model_name='serviciolegal',
            old_name='nombre_servicio',
            new_name='_nombre_servicio',
        ),
    ]
