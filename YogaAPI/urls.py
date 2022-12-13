from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from YogaAPI import views
urlpatterns = [
    path('api/batch', views.BatchList.as_view()),
    # User List
    path('api/user', views.RegisterUser.as_view()),
    path('api/user/<int:pk>', views.RegisteredUser.as_view()),
    # BookedBatchList
    path('api/booked', views.BookedBatchList.as_view()),
    # PaymentList
    path('api/payment', views.PaymentList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)