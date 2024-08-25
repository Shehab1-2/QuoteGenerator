from django.urls import path
from .views import get_random_quote, save_quote, get_saved_quotes

urlpatterns = [
    path('api/quotes/', get_random_quote, name='get_random_quote'),
    path('api/save-quote/', save_quote, name='save_quote'),
    path('api/saved-quotes/', get_saved_quotes, name='get_saved_quotes'), 
]
