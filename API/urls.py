from django.urls import path,include


app_name ="api"

urlpatterns = [
    path('payment/', include("API.payment.urls",namespace="payment_api")),
]
