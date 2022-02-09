from django.urls import path
from .views import home, c1, c2

urlpatterns = [
    path('', home, name="home"),
    path('c1/', c1, name="c1"),
    path('c2/', c2, name="c2"),
]