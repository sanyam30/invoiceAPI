from rest_framework import serializers
from .models import Invoice,File

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invoice
		fields = ('invoiceNum','status')

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('invoiceNum','file','timestamp')

class InvoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Invoice
		fields = '__all__'
			