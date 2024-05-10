from django.db import models
from shared.models import BaseModel

class Services(BaseModel):
    name = models.CharField(max_length = 100, null=False, blank=False)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    sub_heading = models.CharField(max_length = 100, null = True, blank = True)
    sub_description = models.TextField(null = True, blank = True)
    sub_heading2 = models.CharField(max_length = 100, null = True, blank = True)
    sub_description2 = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Services"