from django.db import models


class CPUData(models.Model):
    date = models.CharField(max_length=100, blank=True, null=True, verbose_name='Дата записи')
    cpu = models.FloatField(verbose_name='Утилизация CPU в %')

    class Meta:
        verbose_name = 'Основную информацию'
        verbose_name_plural = 'Основная информация'
