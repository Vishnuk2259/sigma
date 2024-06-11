from django.db import models
from shared.models import BaseModel

class Banner(BaseModel):
    page_url = models.CharField(max_length = 255, choices=[('/index', 'Index'), ('/clients', 'Clients'), ('/contact', 'Contact',), ('/facilities', 'Facilities'), ('/service', 'Service'), ('/gallery', 'Gallery'), ('/partners', 'Partners'), ('/profile', 'Profile'), ('/team', 'Team')], null = True, blank = True)
    banner_type = models.CharField(max_length = 100, choices=[('Header', 'Header'), ('Footer', 'Footer'), ('Body', 'Body')], null = True, blank = True)
    content = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    title = models.CharField(max_length = 255, null = True, blank = True)
    about = models.CharField(max_length = 255, choices=[('Hero banner', 'Hero banner'), ('Body banner', 'Body banner'), ('What we do', 'What we do'), ('What we do content', 'What we do content'), ('Team', 'Team'), ('Partners', 'Partners'), ('Why sigma', 'Why sigma'), ('Get in touch', 'Get in touch'), ('Mission', 'Mission'), ('Vision', 'Vision'), ('Value', 'Value')], null = True, blank = True)
    
    def __str__(self):
        return f"{self.title} , {self.id}"