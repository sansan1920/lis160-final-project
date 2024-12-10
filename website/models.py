from django.db import models

# Create your models here.
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	genre = models.CharField(max_length=20)
	status = models.BooleanField(default=False)
	curr_chapt = models.CharField(max_length=20, null=True)

def __str__(self):
	return(f"{self.title}")