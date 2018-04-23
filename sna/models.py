from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


STYLE_CHOICES = (('Straight', 'straight'), ('Curvy', 'curvy'),)


class GephiVis(models.Model):
    description = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='sna_assets/', max_length=500)
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, default='Curvy')

    def __unicode__(self):
        return u'%s' % self.description


rgb_validators = [
    MaxValueValidator(255),
    MinValueValidator(0)
]


class LegendItem(models.Model):
    visualisation = models.ForeignKey('GephiVis')
    category_description = models.CharField(max_length=50)
    red = models.IntegerField(default=255, \
                              validators=rgb_validators)
    green = models.IntegerField(default=255, \
                                validators=rgb_validators)
    blue = models.IntegerField(default=255, \
                               validators=rgb_validators)

    def __unicode__(self):
        return u'%s, %s' % (self.category_description, self.visualisation)
