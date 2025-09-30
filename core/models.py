from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text='Comma seperated list of technologies used')
    live_url = models.URLField(max_length=200, blank=True,null=True)
    github_url = models.URLField(max_length=200, blank=True,null=True)
    image = models.ImageField(upload_to='static/portfolio_images/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    