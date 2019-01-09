from django.db import models

# Create your models here.

class furniture(models.Model):
	furniture_id = models.IntegerField(blank=True)
	name = models.CharField(max_length=30)
	category = models.CharField(max_length=20)
	description = models.TextField()
	purchase_date = models.DateField(auto_now=True)
	purchase_price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
	purchase_customer_id = models.IntegerField()
	item_sold = models.BooleanField(default=False)
	sale_date = models.DateField(null=True)
	sale_price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
	sale_customer_id = models.IntegerField(null=True)

	def add(self):
		self.furniture_id = getNextFurnitureId()
		self.save()

	def __str__(self):
		return self.name

class customers(models.Model):
	customer_id = models.IntegerField()
	f_name = models.CharField(max_length=20)
	l_name = models.CharField(max_length=20)
	address_1 = models.CharField(max_length=30)
	address_2 = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	post_code = models.CharField(max_length=10)
	tel_no = models.CharField(max_length=15)
	notes = models.TextField()

	def add(self):
		self.save()

	def __str__(self):
		return self.f_name + ' ' + self.l_name

class image(models.Model):
	furniture_id = models.IntegerField()
	image_id = models.IntegerField()
	description = models.TextField()

	def add(self):
		self.image_id = getNextImageId(self.furniture_id)
		self.save()

	def __str__(self):
		return self.description

def getNextFurnitureId():
	if not furniture.objects.all():
		return 0
	else:
		return furniture.objects.all().order_by('-furniture_id')[0].furniture_id+1

def getNextImageId(furnitureId):
	if not image.objects.filter(furniture_id = furnitureId):
		return 0
	else:
		return image.objects.filter(furniture_id = furnitureId).order_by('-image_id')[0].image_id
