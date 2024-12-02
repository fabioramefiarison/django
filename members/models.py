from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField()
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  from django.db import models
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}"