from django.db import models

class Item(models.Model):
  item_name = models.CharField(max_length=100)
  item_quantity = models.IntegerField()

  def __str__(self):
      return self.item_name

class Vendor(models.Model):
  vendor_name = models.CharField(max_length=100)

  def _str_(self):
      return self.vendor_name

class Customer(models.Model):
  customer_name = models.CharField(max_length=100)

  def _str_(self):
      return self.customer_name
