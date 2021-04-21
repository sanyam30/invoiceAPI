from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StatusSerializer,InvoiceSerializer,FileSerializer
from .models import Invoice,File
from django.core.exceptions import ObjectDoesNotExist


#Returns the list of api's available
@api_view(['GET'])
def api_overview(request):
	res = {
		'Upload Invoice':'http://localhost:8000/api/upload-invoice',
		'Get Invoice':'http://localhost:8000/api/get-invoice/<int:invoiceNum>',
		'Mark Digitized':'http://localhost:8000/api/mark-digitized',
		'Get Status':'http://localhost:8000/api/status/<int:invoiceNum>',
		'Add Invoice':'http://localhost:8000/api/add-invoice'
	}
	return Response(res,status=status.HTTP_200_OK)

#GET to return the status of invoice 
@api_view(['GET'])
def get_status(request,invoiceNum):
	try:
		invoice = Invoice.objects.get(invoiceNum=invoiceNum)
		serializer = StatusSerializer(invoice)
		return Response(serializer.data,status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		res = {
		 "error":"Invoice doesn't exist"
		}
		return Response(res,status=status.HTTP_400_BAD_REQUEST)

#POST to update the status of a particular invoice to DIGITIZED
@api_view(['POST'])
def update_status(request):
	#Checking if request contains invoice number 
	try:
		invoiceNum = request.data['invoiceNum']
		invoice = Invoice.objects.filter(invoiceNum=invoiceNum)
		#If invoice exists status is updated
		if invoice:
			invoice = Invoice.objects.get(invoiceNum = invoiceNum)
			invoice.status = "DIGITIZED"
			invoice.save()
			serializer = StatusSerializer(invoice)
			return Response(serializer.data,status=status.HTTP_200_OK)

		#Error message returned if doesn't exists
		else:
			res = {
			"error":"Invoice doesn't exists"
			}
			return Response(res,status=status.HTTP_400_BAD_REQUEST)

	except KeyError:
		res = {
		"error":"Invoice number wasn't passed"
		}
		return Response(res,status=status.HTTP_400_BAD_REQUEST)


#POST and PATCH for adding/updating an invoice
@api_view(['POST','PATCH'])
def add_invoice(request):
	'''
	PATCH will be used whenever a new invoice is added or want 
	to update any previous one
	'''
	if request.method == 'PATCH':
		try:
			invoiceNum = request.data['invoiceNum']
			invoice = Invoice.objects.filter(invoiceNum=invoiceNum)
			if invoice:
				invoice = Invoice.objects.get(invoiceNum=invoiceNum)
				for i in request.data:
					setattr(invoice,i,request.data.get(i))
					invoice.save()
				serializer = InvoiceSerializer(invoice)
				return Response(serializer.data,status=status.HTTP_200_OK)
			else:
				serializer = InvoiceSerializer(data=request.data,partial = True)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data,status=status.HTTP_200_OK)
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except KeyError:
			res = {
			"error":"Invoice number not passed"
			}
			return Response(res,status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'POST':
		'''
		POST just in case if an invoice is to be added from scratch
		'''
		serializer = InvoiceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#GET to fetch the details of an invoice
@api_view(['GET'])
def get_invoice(request,invoiceNum):
	try:
		invoice = Invoice.objects.get(invoiceNum=invoiceNum)
		if invoice.status!='DIGITIZED' :
			res = {
			"error":"Invoice yet to be Digitized."
			}
			return Response(res,status.HTTP_200_OK)
		serializer = InvoiceSerializer(invoice)
		return Response(serializer.data,status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		res = {
		 "error":"Invoice doesn't exist"
		}
		return Response(res,status=status.HTTP_400_BAD_REQUEST)

#POST to upload an invoice pdf 
@api_view(['POST'])
def upload_invoice(request):
	file_serializer = FileSerializer(data=request.data)
	if file_serializer.is_valid():
		file_serializer.save()
		#Calling this to add the invoice to db and set status as uploaded
		request._request.method = 'PATCH'
		res = add_invoice(request._request)
		return Response(file_serializer.data,status=status.HTTP_200_OK)
	return Response(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)



