from django.test import TestCase
from django.urls import reverse
from .models import SavedQuote

class QuoteAPITestCase(TestCase):
    
    def test_get_random_quote(self):
        response = self.client.get(reverse('get_random_quote'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', response.json())
        self.assertIn('author', response.json())

    def test_save_quote(self):
        data = {
            "quote": "The only limit to our realization of tomorrow is our doubts of today.",
            "author": "Franklin D. Roosevelt"
        }
        response = self.client.post(reverse('save_quote'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"status": "Quote saved!"})

        # Verify that the quote was saved in the database
        saved_quote = SavedQuote.objects.get(quote=data["quote"], author=data["author"])
        self.assertIsNotNone(saved_quote)

    def test_get_saved_quotes(self):
        # Create a couple of quotes to test retrieval
        SavedQuote.objects.create(quote="The only limit to our realization of tomorrow is our doubts of today.", author="Franklin D. Roosevelt")
        SavedQuote.objects.create(quote="Life is what happens when you're busy making other plans.", author="John Lennon")

        response = self.client.get(reverse('get_saved_quotes'))
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the saved quotes
        data = response.json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["quote"], "The only limit to our realization of tomorrow is our doubts of today.")
        self.assertEqual(data[0]["author"], "Franklin D. Roosevelt")
        self.assertEqual(data[1]["quote"], "Life is what happens when you're busy making other plans.")
        self.assertEqual(data[1]["author"], "John Lennon")
