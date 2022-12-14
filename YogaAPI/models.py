from django.db import models


class Register(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, blank=True, default='')
    idproof = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=10, unique=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.phone
    
    class Meta:
        ordering = ['created']
    

class Batch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    batch = models.CharField(max_length=20, blank=False, unique=True)
    class Meta:
        ordering = ['created']


allBatch = list(set(Batch.objects.values_list('batch', flat=True)))
tupBatch = sorted([(item, item) for item in allBatch])

qsPhone = list(set(Register.objects.values_list('phone', flat=True)))
tuPhone = sorted([(item, item) for item in qsPhone])

class BookedBatch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(choices=tuPhone, blank=True, null=True, max_length=10)
    slot = models.CharField(choices=tupBatch, blank=True,
                            null=True, max_length=10)
    slotBooked = models.DateField()
    class Meta:
        ordering = ['created']

class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(choices=tuPhone, blank=True, null=True, max_length=10)
    paymentId = models.CharField(max_length=20, blank=True, default='')
    datePaid = models.DateField()
    amount = models.IntegerField(blank=True, default='000')
    class Meta:
        ordering = ['created']
