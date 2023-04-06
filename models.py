from django.db import models

class register(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
def _str_(self):
    return self.username
class meta:
    db_table = "studentregistration"