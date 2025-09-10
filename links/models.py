from django.db import models
from django.utils.text import slugify
# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    url = models.URLField(max_length= 200)
    slug = models.SlugField(unique=True , blank = True)
    clicks  = models.PositiveBigIntegerField(default= 0)
    #create built-in function that can  return string output
    def __str__(self):
        #return output as a string
        return f"{self.name} | {self.clicks}"
    #create method for increment the atrribute 
    def click(self):
        self.clicks += 1
        self.save()
    #overwrite the save method to  
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)