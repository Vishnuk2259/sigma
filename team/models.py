from django.db import models
from shared.models import BaseModel

class Team(BaseModel):
    name = models.CharField(max_length = 100, null=False, blank=False)
    member_category = models.CharField(max_length = 100, choices =[('Top management team', 'Top management team'), ('Engineering team', 'Engineering team')], null = True, blank = True)
    member_designation = models.CharField(max_length = 100, null = True, blank = True)
    image = models.ImageField(upload_to = 'team/logos', null = True, blank = True)
    linkedin = models.URLField(null = True, blank = True)
    
    def __str__(self):
        return self.name

