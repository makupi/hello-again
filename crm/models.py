from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=16)
    city_code = models.CharField(max_length=18)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)


class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=32)
    customer_id = models.BigIntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustomerRelationship(models.Model):
    appuser = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    points = models.IntegerField()
    last_activity = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    