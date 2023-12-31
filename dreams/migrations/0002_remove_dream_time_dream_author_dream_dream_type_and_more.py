# Generated by Django 4.2.7 on 2023-12-02 02:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dreams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dream',
            name='time',
        ),
        migrations.AddField(
            model_name='dream',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dream_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dream',
            name='dream_type',
            field=models.CharField(choices=[('SONHO', 'Sonho'), ('PESADELO', 'Pesadelo')], default='SONHO', help_text='Sonho / Pesadelo help text', max_length=20, verbose_name='Sonho / Pesadelo'),
        ),
        migrations.AddField(
            model_name='dream',
            name='text',
            field=models.TextField(default='[ sonho sem conteúdo ]', help_text='Conteúdo do sonho', verbose_name='dream_text'),
        ),
        migrations.AlterField(
            model_name='dream',
            name='title',
            field=models.CharField(default='[ sonho sem título ]', help_text='Título do sonho', max_length=50, verbose_name='dream_title'),
        ),
    ]
