from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from YogaAPI import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# data = {'get': 'list', 'post': 'create'}
# router.register('user', views.RegisteredUser().as_view(), basename='user')
# router.register('payment', views.PaymentList.as_view(), basename='payment')

urlpatterns = [
    # path('', include(router.urls)),
    path('batch', views.BatchList.as_view()),
    # User List
    path('user', views.RegisterUser.as_view(), name='user'),
    path('user/<int:pk>', views.RegisteredUser.as_view()),
    # BookedBatchList
    path('booked', views.BookedBatchList.as_view()),
    # PaymentList
    path('payment', views.PaymentList.as_view(), name='payment'),
]

urlpatterns = format_suffix_patterns(urlpatterns)