from django.db import models

# Create your models here.
class Prompt(models.Model):
    idea = models.TextField()
    category = models.TextField()
    label = models.TextField()

    def __str__(self):
        return self.idea


class Playwright(models.Model):
    name = models.TextField()
    email = models.TextField()
    prompt = models.ForeignKey(Prompt, 
    on_delete=models.CASCADE,
    related_name='assignments')

    def __str__(self):
        return self.name
