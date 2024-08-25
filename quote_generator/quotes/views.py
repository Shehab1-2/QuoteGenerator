# quotes/views.py

import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SavedQuote

# List of quotes
QUOTES = [
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Life is what happens when you’re busy making other plans.", "author": "John Lennon"},
    {"quote": "Get busy living or get busy dying.", "author": "Stephen King"},
    {"quote": "You only live once, but if you do it right, once is enough.", "author": "Mae West"},
    {"quote": "Many of life’s failures are people who did not realize how close they were to success when they gave up.", "author": "Thomas A. Edison"},
]

def get_random_quote(request):
    quote = random.choice(QUOTES)
    return JsonResponse(quote)



@csrf_exempt 
def save_quote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        quote = data.get('quote')
        author = data.get('author')

        # Save to database
        SavedQuote.objects.create(quote=quote, author=author)

        return JsonResponse({'status': 'Quote saved!'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_saved_quotes(request):
    saved_quotes = SavedQuote.objects.all().values('quote', 'author')
    return JsonResponse(list(saved_quotes), safe=False)