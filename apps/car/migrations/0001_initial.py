# Generated by Django 4.2.7 on 2023-11-15 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('mileage', models.IntegerField()),
                ('volume', models.DecimalField(decimal_places=1, max_digits=2)),
                ('fuel', models.CharField(max_length=20)),
                ('engine', models.CharField(max_length=10)),
                ('drive_unit', models.CharField(max_length=20)),
                ('kpp', models.CharField(max_length=20)),
                ('str_wheel', models.CharField(max_length=20)),
                ('preview', models.ImageField(blank=True, upload_to='previews/')),
                ('city', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Тачка',
                'verbose_name_plural': 'Тачки',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='car.car')),
            ],
        ),
    ]
