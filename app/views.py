from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.

class Product_crud(APIView):
    def get(self,request,pk):
        rbd=Product.objects.all()
        pjd=ProductMS(rbd, many=True)
        return Response(pjd.data)
    
    def post(self,request,pk):
        pmsd=ProductMS(data=request.data)
        if pmsd.is_valid():
            pmsd.save()
            return Response({"success":"data is inserted successfull"})
        else:
            return Response({"failed":"inserting data fail"})
        
    def put(self,request,pk):
        instance=Product.objects.get(pk=pk)
        list_pyhton_object=ProductMS(instance,data=request.data)
        if list_pyhton_object.is_valid():
            list_pyhton_object.save()
            return Response({'update':"data is updated"})
        return Response({'fail':'data is fail to update'})
    
    def patch(self,request,pk):
        instance=Product.objects.get(pk=pk)
        lpo=ProductMS(instance,data=request.data,partial=True)
        if lpo.is_valid():
            lpo.save()
            return Response({'partial':'data is updated'})
        return Response({'failed':'data is not updated'})
    
    def delete(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'delete':'data is deleted succfully'})
    