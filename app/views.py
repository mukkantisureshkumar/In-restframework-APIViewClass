from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.

class Product_crud(APIView):
    def get(self,request):
        rbd=Product.objects.all()
        pjd=ProductMS(rbd, many=True)
        return Response(pjd.data)
    
    def post(self,request):
        pmsd=ProductMS(data=request.data)
        if pmsd.is_valid():
            pmsd.save()
            return Response({"success":"data is inserted successfull"})
        else:
            return Response({"failed":"inserting data fail"})
        
