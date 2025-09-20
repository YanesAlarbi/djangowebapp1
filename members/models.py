from django.db import models

# Create your models here.


class Member(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone_num=models.CharField(max_length=20,null=True)
    join_date=models.DateField(null=True)


    # def __str__(self):
    #        return f"{self.fname} {self.lname}"


