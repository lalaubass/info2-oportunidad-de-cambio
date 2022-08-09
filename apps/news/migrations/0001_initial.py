# Generated by Django 4.0.6 on 2022-08-03 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('imagen', models.ImageField(default='news/default.png', upload_to='news')),
                ('Categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.categorias')),
            ],
        ),
    ]