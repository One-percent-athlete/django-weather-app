from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=50, blank=True, null=True)
    lon = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return f"City Name: {self.name} - City Id: {self.id} - lat:{self.lat}, lon:{self.lon}"