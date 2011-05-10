import simplejson
import datetime
import base64
from webservice_tools import utils
from webservice_tools.decorators import login_required
from django.db import transaction

class AppleRecieptHandler(utils.BaseHandler):
    """
    Handler for utilizing apple's in app purchase
    Usage:
      place webservice_tools.apps.inapp_purchase in your 'INSTALLED_APPS'
      import this handler, subclass it
      define a 'redeem' method, that will get passed the apple_receipt (see below for signature)
      grant the user your product in that method, if it gets called, the receipt has been verified
       and entered into the database, (subsequent calls for the same receipt will be rejected)
       you can use apple_receipt.product_id to look up the product
       
     point a url to your handler
      
    """
   
    allowed_methods = ('POST',)
    
    @login_required
    @transaction.commit_manually
    def create(self, request, response):
        """
        Receives receipt from client, verifies with apple, makes necessary db changes to provide the product
        API Handler: POST /receipt
        PARAMS:
            @receipt_data [string]: this is the receipt data apple gave you in the transactionReceipt property of your receipt 
        """ 
        receipt_data = request.POST.get('receipt_data')
        profile = request.user.get_profile()
        if not receipt_data:
            transaction.rollback()
            return response.send(errors='Please provide the data from "transactionReceipt" in order to process your purchase')
        
        encoded_data = base64.b64encode(receipt_data)
        json_data = simplejson.dumps({"receipt-data": encoded_data})
        result = utils.makeAPICall(consts.APPLE_STORE_URL, consts.VERIFY_RECIEPT_API_HANDLER, rawPostData=json_data, secure=True)
        if not result['status'] == 0:
            response.set(apple_response=result)
            transaction.rollback()
            return response.send(errors='Invalid receipt', status=500)
        
        receipt = result['receipt']
        try:
            AppleReceipt.objects.get(original_transaction_id=receipt['original_transaction_id'])
            transaction.rollback()
            return response.send(errors="Invalid receipt", status=500)
        except AppleReceipt.DoesNotExist:
            pass
        
        receipt['purchase_date'] = datetime.datetime.strptime(receipt['purchase_date'], "%Y-%m-%d %H:%M:%S Etc/%Z")
        receipt['original_purchase_date'] = datetime.datetime.strptime(receipt['original_purchase_date'], "%Y-%m-%d %H:%M:%S Etc/%Z")
        receipt['profile'] = profile
        apple_receipt = AppleReceipt.objects.create(**receipt)
        
        transaction.commit()
        return self.redeem(apple_receipt, response)
        
    
    def redeem(self, apple_receipt, response):
        """
        After an apple receipt is posted, the handler will call this method,
        Do what you need to do and return response.send() (you can look up your purchased product via apple_receipt.product_id
        """
        raise NotImplementedError