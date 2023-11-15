from django.db import models

class Dream(models.Model):
    """descrição"""

    DREAM_TIME = (
        ('DIA', 'Diurno'),
        ('NOITE', 'Noturno'),
        ('INDEFINIDO', 'Não presenciado')
    )

    # CAMPOS
    title = models.CharField(
        verbose_name="dream_title",
        max_length=50,
        help_text="Título do sonho",
    )
    time = models.CharField(
        verbose_name="Estado do dia no sonho",
        max_length=50,
        default="INDEFINIDO",
        help_text="dia / noite no sonho",
        choices=DREAM_TIME
    )

    def __str__(self):
        """String para representar o objeto Dream (no site Admin)."""
        return f"Sonho ${ self.title }"

# Create your models here.
