from django.db import models


class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class Address(models.Model):
    address = models.TextField(null=True, blank=True)
    people = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    def __str__(self):
        return self.address
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    people = models.ForeignKey(
        People,
        on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Bio(models.Model):
    content = models.TextField(null=True, blank=True)
    people = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.content