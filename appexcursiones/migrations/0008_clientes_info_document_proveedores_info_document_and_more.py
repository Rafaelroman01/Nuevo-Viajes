# Generated by Django 4.1.3 on 2023-10-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appexcursiones', '0007_rename_info_documentacion_documentacion_info_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='info_document',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='proveedores',
            name='info_document',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='recreadores',
            name='info_document',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='viajes',
            name='info_document',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
