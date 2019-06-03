from django.db import models


class TypeItem(models.Model):
    description = models.CharField('Descrição', max_length=150, blank=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Descrição'
        verbose_name_plural = 'Descrições'


class Item(models.Model):
    type = models.ForeignKey(TypeItem, related_name='Descrição', blank=False, on_delete=models.CASCADE)
    stock_code = models.IntegerField('Código Interno', blank=True, null=True)
    name = models.CharField('Nome', max_length=100, blank=False)
    diameter = models.DecimalField('Diametro', max_digits=5, decimal_places=2, blank=False)
    cutterLength = models.DecimalField('Altura de Corte', max_digits=5,decimal_places=2, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nome'
        verbose_name_plural = 'Nomes'
        ordering = ['diameter']