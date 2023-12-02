from django.db import models
from django.contrib.auth.models import User

class Dream(models.Model):
    DREAM_TYPE = (
        ('SONHO', 'Sonho'),
        ('PESADELO', 'Pesadelo'),
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
        max_length=50,
        help_text="Título do sonho",
        default="[ sonho sem título ]"
    )
    text = models.TextField(
        verbose_name="dream_text",
        help_text="Conteúdo do sonho",
        default="[ sonho sem conteúdo ]"
    )
    dream_type = models.CharField(
        verbose_name="Sonho / Pesadelo",
        max_length=20,
        default="SONHO",
        help_text="Sonho / Pesadelo help text",
        choices=DREAM_TYPE
    )
    date = models.DateField(
        verbose_name="dream_date",
        auto_now=True
    )

    def __str__(self):
        """String para representar o objeto Dream (no site Admin)."""
        return f"Sonho ${ self.title }"
