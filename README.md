# invoiceAPI

To run the project 

1. python -m venv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python manage.py runserver
5. go to http://localhost:8000/api/


The Project has 5 API's

1. Upload Invoice

   Endpoint URL -> http://localhost:8000/api/upload-invoice
   
   
   Request type: POST
   
   
   Parameters required:
      invoiceNum, file
     

2. Get Status 

    Endpoint URL -> http://localhost:8000/api/status/<int:invoiceNum>
    
    Request type: GET
    
3. Get Invoice

   Endpoint URL -> http://localhost:8000/api/get-invoice/<int:invoiceNum>
   
   Request type: GET

4. Update Invoice


   Endpoint URL -> http://localhost:8000/api/update-invoice
   
   Request type: PATCH
   
   parameter required:
   
   {
   
    "invoiceNum" : (mandatory) ,
    
    "invoiceDate":"",
    
    "buyer": "",
    
    "buyerAddress" :"",
    
    "seller" : "",
    
    "sellerAddress" : "",
    
    "lineItems": "[{'item':'','cost':'','qty':'','amount':''}]",
    
    "subtotal" :,
    
    "tax" :,
    
    "totalAmount" :
    
  }


5. Mark Digitized


   Endpoint URL -> http://localhost:8000/api/mark-digitized
   
   Request type: POST
   
   parameter required:
   
   {"invoiceNum":<number>}(mandatory)
