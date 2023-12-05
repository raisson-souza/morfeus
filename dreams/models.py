from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Dream(models.Model):
    DREAM_TYPE = (
        ('Sonho', 'Sonho'),
        ('Pesadelo', 'Pesadelo')
    )

    FEELINGS = (
        ('Normal', 'Normal'),
        ('Feliz', 'Feliz'),
        ('Triste', 'Triste'),
        ('Raivoso', 'Raivoso'),
        ('Asssustado', 'Asssustado'),
        ('Indefinido', 'Indefinido'),
        ('Múltiplos', 'Múltiplos')
    )

    LUCID = (
        ('Não Lúcido', 'Não Lúcido'),
        ('Parcialmente Lúcido', 'Parcialmente Lúcido'),
        ('Lúcido', 'Lúcido')
    )

    PERIODS = (
        ('Dia', 'Dia'),
        ('Noite', 'Noite'),
        ('Indefinido', 'Indefinido'),
        ('Múltiplos', 'Múltiplos'),
    )

    # CAMPOS
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dream_user',
        default=1
    )
    title = models.CharField(
        verbose_name="dream_title",
        help_text="Título do sonho",
        max_length=50,
        default="[ sonho sem título ]"
    )
    text = models.TextField(
        verbose_name="dream_text",
        help_text="Conteúdo do sonho",
        default="[ sonho sem conteúdo ]"
    )
    dream_type = models.CharField(
        verbose_name="dream_type",
        help_text="Tipo de Sonho",
        max_length=10,
        default="Sonho",
        choices=DREAM_TYPE
    )
    feeling = models.CharField(
        verbose_name="feeling",
        help_text="Sentimento",
        default="Indefinido",
        choices=FEELINGS,
        max_length=20
    )
    lucid = models.CharField(
        verbose_name="lucid",
        help_text="Lucidez",
        default="Não Lúcido",
        choices=LUCID,
        max_length=20
    )
    period = models.CharField(
        verbose_name="period",
        help_text="Período",
        default="Indefinido",
        choices=PERIODS,
        max_length=20
    )
    date = models.DateField(
        verbose_name="dream_date"
    )
    public = models.BooleanField(
        verbose_name="public",
        help_text="Sonho Público",
        default=False
    )

    def __str__(self):
        """String para representar o objeto Dream (no site Admin)."""
        return f"Sonho { self.title } / Autor { self.author }"
