# Generated by Django 4.0.4 on 2022-05-31 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('coat', models.CharField(choices=[('BLK', 'Black'), ('BLK & CREAM', 'Black & Cream'), ('BLK & Red', 'Black & Red'), ('BLK & SILVER', 'Black & Silver'), ('BLK & TAN', 'Black & Tan'), ('BLUE', 'Blue'), ('GRAY', 'Gray'), ('LIVER', 'Liver'), ('SABLE', 'Sable'), ('WHITE', 'White'), ('BI-COLOR', 'Bi-Color')], max_length=64)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('description', models.TextField()),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
