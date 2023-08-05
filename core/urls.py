from django.urls import path
from .views import HomePageView, handler404 as custom_handler404

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
]

handler404 = custom_handler404