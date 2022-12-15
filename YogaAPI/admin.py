from django.contrib import admin
from .models import Payment ,Register, Batch, BookedBatch


class RegisterTable(admin.ModelAdmin):
    list_display = ('phone', 'id', 'created', 'username', 'idproof', 'address')
admin.site.register(Register, RegisterTable)


class BatchTable(admin.ModelAdmin):
    list_display = ('id', 'created', 'batch')
admin.site.register(Batch, BatchTable)


class BookBatchTable(admin.ModelAdmin):
    list_display = ('phone', 'id', 'created', 'slot', 'slotBooked')
admin.site.register(BookedBatch, BookBatchTable)


class PaymentTable(admin.ModelAdmin):
    list_display = ('id', 'created', 'phone', 'paymentId', 'datePaid', 'amount')
admin.site.register(Payment, PaymentTable)