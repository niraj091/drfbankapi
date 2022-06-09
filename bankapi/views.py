from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bankapi.serializers import BankSerializer
from rest_framework import status
from bankapi.utils import get_object_by_bank_name,get_object_by_ifsc

class BankDetails(APIView):
    def get(self,request,*args,**kwargs):
        if request.query_params :
            if 'bank_name' in request.query_params:
                bank_name = request.query_params["bank_name"].upper()
                city = request.query_params["city"].upper()
                bank_details = get_object_by_bank_name(bank_name,city)

                if bank_details is None:
                    return Response({"msg":"No match found.Please check the bank name or city and try again."},status=status.HTTP_404_NOT_FOUND)
                serializer = BankSerializer(bank_details,many=True)
                return Response(serializer.data)


            elif 'ifsc' in request.query_params:
                ifsc = request.query_params["ifsc"].upper()
                bank_details = get_object_by_ifsc(ifsc)
                if bank_details is None:
                    return Response({"msg":"No match found.Please check the IFSC code and try again."},status=status.HTTP_404_NOT_FOUND)
                serializer=BankSerializer(bank_details)
                return Response(serializer.data)
        return Response({"msg":"Not enough parameters.Please provide bank name and city or IFSC code to get the bank details"},status=status.HTTP_400_BAD_REQUEST)



        
