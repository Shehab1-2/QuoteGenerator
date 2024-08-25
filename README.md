# QUOTE GENERATOR

## Django/React

This quote generator app uses React for the front-end and Django for the back-end.

![Quote Generator Screenshot](assets/img.png)


### Front-End Components:
- `Foot.js`
- `NewQuoteButton.js`
- `SaveQuote.js`
- `SavedQuotes.js`

### Back-End (Django):
The back-end is built using the Django framework and provides the following API endpoints:
- **Quotes API:** `http://127.0.0.1:8000/api/quotes/`
- **Saved Quotes API:** `http://127.0.0.1:8000/api/saved-quotes/`
- **Save Quote API:** `http://127.0.0.1:8000/api/save-quote/`

### Application Features:
- **Quote Rendering:** A random quote is rendered when the site is launched.
- **New Quote Generation:** Users can generate new quotes by clicking the "New Quote" button.
- **Save Quotes:** When the "Save" button is clicked, the corresponding quote is saved to a SQLite database.
- **Database Management:** Although a delete functionality was not implemented, you can clear the database content using the command `python manage.py flush`.

### AWS Deployment:
For deploying this app on AWS:
- Use **Elastic Beanstalk** for an all-in-one environment that handles the Django back-end.
- Use **RDS** (Relational Database Service) for database management.
- Use **S3** (Simple Storage Service) to store the front-end components.

## Testing Overview

This project includes both unit and integration tests to ensure the reliability and correctness of the application.

- **Unit Testing**: The `test_save_quote` method is a unit test that verifies the correct functionality of saving a quote to the database. It ensures that when a quote is submitted through the API, it is properly stored in the database.

- **Integration Testing**: The `test_get_random_quote` and `test_get_saved_quotes` methods are integration tests. These tests validate the interaction between various components of the application, including views, URL routing, and database models. Specifically, they ensure that:
  - The `get_random_quote` API endpoint correctly retrieves a random quote.
  - The `get_saved_quotes` API endpoint accurately returns all saved quotes from the database.

These tests are implemented using Django's testing framework, providing confidence in both individual components and their integration within the overall application.


---
