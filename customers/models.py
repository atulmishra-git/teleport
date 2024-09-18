from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, blank=False)

    class Meta:
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.name


