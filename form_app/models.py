from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=255, default='')
    rating = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    connection_name = models.CharField(max_length=255, default='N/A')
    status = models.CharField(max_length=100)
    date_applied = models.DateField()
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.company
