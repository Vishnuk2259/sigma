from django.db import models
from django.utils import timezone
from datetime import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        
    def strftime_created_at(self):
        return self.created_at.strftime("%d/%m/%Y, %H:%M:%S")
    
    def strftime_updated_at(self):
        return self.updated_at.strftime("%d/%m/%Y, %H:%M:%S")
    
    @classmethod
    def to_datetime(cls, timestamp):
        return datetime.fromtimestamp(timestamp)
    
    @classmethod 
    def to_timestamp(cls, time):
        return datetime.timestamp(time)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)
    

class Gallery(BaseModel):
    image = models.ImageField()
    title = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name_plural = "Gallery"


class Contact(BaseModel):
    name = models.CharField(max_length = 100, null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    phone = models.CharField(max_length = 15, null = True, blank = True)
    message = models.TextField(null = False, blank = False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact"


class Settings(BaseModel):
    name = models.CharField(max_length = 100, null = False, blank = False)
    logo = models.ImageField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    favicon = models.ImageField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    phone = models.CharField(max_length = 15, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    facebook = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name_plural = "Settings"

