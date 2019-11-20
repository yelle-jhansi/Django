# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
 	roles = [("v","Vendor"), ("m","Manager")]
 	address = models.CharField(max_length = 250, blank=True)
 	phone = models.CharField(max_length = 15)
 	role = models.CharField(choices = roles, max_length=2, default = "v")
 	user = models.OneToOneField(User)
 	class Meta:
 		db_table = "userprofile"#overide the table name 
 	def __str__(self):
 		return self.user.username
class ProductCategory(models.Model):
	name = models.CharField(max_length=250, blank=True)
	description = models.TextField()
	class Meta:
		db_table = "product_category"

class Product(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField()
	charge_day  = models.IntegerField(null=True)
	category  = models.ForeignKey(ProductCategory)
	class Meta:
		db_table = "product"
class StockOperation(models.Model):
	name=models.CharField(max_length=250)
	description = models.TextField()
	product=models.ManyToManyField(Product)
	class Meta:
		db_table="stockoperation"
