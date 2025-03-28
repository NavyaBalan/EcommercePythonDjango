# Generated by Django 4.2.2 on 2023-09-06 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0016_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
                ('zip_code', models.IntegerField()),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'), ('Delhi', 'Delhi'), ('TamilNadu', 'TamilNadu'), ('AndhraPredhesh', 'AndhraPradhesh'), ('Rajasthan', 'Rajasthan')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
