from typing_extensions import TypeAlias
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
       db_table = 'menus'

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'categories'
        

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    protein = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)
    
    class Meta:
        db_table = 'nutritions'
        
class Products(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)    
    description = models.TextField(null=True)
    nutrition= models.ForeignKey('Nutritions', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products'    
        
class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    product_id = models.ForeignKey('Products', on_delete=models.CASCADE)        
        
    class Meta:
         db_table = 'images'      
         
class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = 'allergy'
        
class  Allergy_products(models.Model):
    allergy_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product_id = models.ForeignKey('products', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'allergy_products'       