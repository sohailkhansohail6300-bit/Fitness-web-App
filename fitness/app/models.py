from django.db import models


# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=100,null=False)
    whatsapp=models.IntegerField(null=False)
    message=models.TextField(null=True)
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class SEO(models.Model):
    page_name = models.CharField(max_length=100, unique=True)

    title = models.CharField(max_length=200)
    meta_description = models.TextField()
    keywords = models.CharField(max_length=255)

    canonical_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.page_name


    