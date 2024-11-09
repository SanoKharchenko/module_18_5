from django.urls import path
from .views import func_temp, ClTemp

urlpatterns = [
    path('func/', func_temp),
    path('class/', ClTemp.as_view())
]
