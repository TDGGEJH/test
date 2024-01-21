from django.db import models

class Zapis(models.Model):
    name = models.CharField(max_length = 15)
    desk = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"