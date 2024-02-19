from django.db import models

# Create your models here.

class Product(models.Model):

    class Meta:
        app_label = 'dsa_backend'

    name = models.CharField(max_length=80, null=False, blank=False)
    received = models.BooleanField(null=False, blank=False)

class Order(models.Model):
    
    class Meta:
        app_label = 'dsa_backend'

    customerName = models.CharField(max_length=80, null=False, blank=False)
    orderNumber = models.IntegerField(null=False, blank=False)
    orderedCases = models.IntegerField(null=False, blank=False)
    actualCases = models.IntegerField(null=False, blank=False)
    estimatedWeight = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    actualWeight = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=80, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # protect means that Order will not be deleted when product is deleted