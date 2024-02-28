from django.db import models

# Create your models here.

class userInfo(models.Model):
   name  = models.CharField(max_length=100)
   email  = models.EmailField()
   password  = models.CharField(max_length=100)

   def __str__(self) -> str:
      return self.name

class todo(models.Model):
   userID = models.IntegerField()
   name =models.CharField(max_length=100)
   description = models.TextField()
   status_choices = [
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]
   status = models.CharField(max_length=10, choices=status_choices, default='todo', )
   def __str__(self):
        return self.name