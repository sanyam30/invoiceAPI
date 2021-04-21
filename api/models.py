from django.db import models
from jsonfield import JSONField
from django.core.validators import FileExtensionValidator
# Create your models here.


class File(models.Model):
  invoiceNum = models.IntegerField(blank=False)
  file = models.FileField(upload_to="invoices",blank=False, null=False,validators=[FileExtensionValidator(['pdf'])])
  timestamp = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
	"""
		Datafields required while adding a new invoice
	"""
	invoiceNum = models.IntegerField(primary_key=True)
	invoiceDate = models.CharField(max_length=20,default="")
	buyer = models.CharField(max_length=100)
	buyerAddress = models.CharField(max_length=1000,default="")
	seller = models.CharField(max_length=100)
	sellerAddress = models.CharField(max_length=1000,default="")
	lineItems = JSONField()
	subtotal = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
	tax = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
	totalAmount = models.DecimalField(max_digits=20,decimal_places = 2,default=0)
	status = models.CharField(max_length=100,default="Uploaded")



	def __str__(self):
		return str(self.invoiceNum)


