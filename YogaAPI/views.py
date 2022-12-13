from .models import Register, Batch, BookedBatch, Payment
from .serializers import RegisterSerializer, BatchSerializer, BookedBatchSerializer, PaymentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class RegisterUser(APIView):

    def get(self, request, format=None):
        qsRegister = Register.objects.all()
        serializer = RegisterSerializer(qsRegister, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisteredUser(APIView):
    
    def get_object(self, pk):
        try:
            return Register.objects.get(phone=pk)
        except Register.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        qsRegister = self.get_object(pk)
        serializer = RegisterSerializer(qsRegister)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        qsRegister = self.get_object(pk)
        serializer = RegisterSerializer(qsRegister, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BatchList(APIView):

    def get(self, request, format=None):
        qsBatch = Batch.objects.all()
        serializer = BatchSerializer(qsBatch, many=True)
        return Response(serializer.data)
    

class BookedBatchList(APIView):

    def get(self, request, format=None):
        qsBookedBatch = BookedBatch.objects.all()
        serializer = BookedBatchSerializer(qsBookedBatch, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BookedBatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentList(APIView):

    def get(self, request, format=None):
        qsPayment = Payment.objects.all()
        serializer = PaymentSerializer(qsPayment, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


