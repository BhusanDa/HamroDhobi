from django.db import models

# Create your models here.
class Order(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phone=models.BigIntegerField()
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    clothtype=models.CharField(max_length=50)
    choose_service=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

#what you want to show in admin panel name or address or anything
#tab should be given after defining function
#alignment should right i.e as below otherwise this won't work
    order="Order Request From"
    def __str__(self):
        return self.order+" "+self.firstname

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    feedback="Feedback From"
    def __str__(self):
        return self.feedback+" "+self.name