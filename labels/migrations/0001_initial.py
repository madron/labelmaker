# Generated by Django 4.2.7 on 2023-11-13 18:58

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import labels.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('background', colorfield.fields.ColorField(blank=True, default='', image_field=None, max_length=25, samples=None)),
                ('image', models.FileField(blank=True, upload_to=labels.utils.get_style_image_path)),
            ],
            options={
                'verbose_name': 'style',
                'verbose_name_plural': 'styles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('text', models.TextField(blank=True)),
                ('style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='labels', to='labels.style', verbose_name='style')),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
                'ordering': ['name'],
            },
        ),
    ]
