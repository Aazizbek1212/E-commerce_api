from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name


