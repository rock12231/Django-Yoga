from .models import Register, Batch, BookedBatch, Payment
from .serializers import RegisterSerializer, BatchSerializer, BookedBatchSerializer, PaymentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BatchList(APIView):

    def get(self, request, format=None):
        qsBatch = Batch.objects.all()
        serializer = BatchSerializer(qsBatch, many=True)
        return Response(serializer.data)



