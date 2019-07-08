from django.urls import path
from . import views
import portfolio.views

urlpatterns = [
    path('', portfolio.views.portfolio, name='portfolio'),
]