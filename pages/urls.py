from django.urls import path
from .views import hello_home_page

app_name = 'pages'
urlpatterns = [
    path('', hello_home_page, name="homepage")
]
