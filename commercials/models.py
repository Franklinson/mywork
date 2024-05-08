from django.db import models

# Create your models here.


class Label(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    # pub_date = models.DateTimeField(auto_now=True)
    


class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.abbreviation}'


class Nutrient(models.Model):
    CATEGORIES = (
        ('TINNED FOODS', 'TINNED FOODS'), 
        ('INSTANT STAPLES', 'INSTANT STAPLES'), 
        ('DAIRY & CREAMERS', 'DAIRY & CREAMERS'),
        ('OILS', 'OILS'),
        ('BISCUITS', 'BISCUITS'),
        ('BEVERAGES', 'BEVERAGES'),
        ('SPREADS, DRESSINGS & SAUCES', ' SPREADS, DRESSINGS & SAUCES'),
        ('GRAINS & CEREALS', 'GRAINS & CEREALS'),
        ('PASTA', 'PASTA'),
        ('INFANT FORMULAE', 'INFANT FORMULAE'),
        ('NUTRITION SUPPLEMENTS', 'NUTRITION SUPPLEMENTS'),
        ('SPICES', 'SPICES'),
    )
    nutrient = models.CharField(max_length=100, choices=CATEGORIES, blank=True)
    name = models.ForeignKey(Label, null=True, on_delete=models.SET_NULL, blank=True)
    value = models.FloatField(max_length=50, null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return f'{self.nutrient}'



    





