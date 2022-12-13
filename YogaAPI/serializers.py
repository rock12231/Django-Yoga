from rest_framework import serializers
from .models import Register, Batch, BookedBatch, Payment


class RegisterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    idproof = serializers.CharField(required=False, allow_blank=True, max_length=100)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return Register.objects.create(**validated_data)
    
class BatchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    batch = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return Batch.objects.create(**validated_data)
    
class BookedBatchSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=False)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=100)
    slot = serializers.CharField(required=False, allow_blank=True, max_length=100)
    datePaid = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return BookedBatch.objects.create(**validated_data)
    
class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(required=False)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=100)
    paymentId = serializers.CharField(required=False, allow_blank=True, max_length=100)
    datePaid = serializers.CharField(required=False, allow_blank=True, max_length=100)
    amount = serializers.CharField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.paymentId = validated_data.get('paymentId', instance.paymentId)
        instance.datePaid = validated_data.get('datePaid', instance.datePaid)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance