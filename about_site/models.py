from django.db import models
import base64


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="img")
    base_64 = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Project, self).save(*args, **kwargs)


