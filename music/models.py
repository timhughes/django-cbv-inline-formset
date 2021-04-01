from django.db import models

# Create your models here.



class Album(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Track(models.Model):
    id = models.BigAutoField(primary_key=True)
    album = models.ForeignKey('Album', null=False, on_delete=models.CASCADE,)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['number']

    def __str__(self):
        return "%s - %s" %( self.number, self.name)

